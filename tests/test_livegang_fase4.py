import asyncio
import json
import gzip
import os
import re
import smtplib
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

from app import create_app
from siteconfig import PUBLIC_PAGES, SITE_URL
from test_livegang_fase1 import Markup
from test_livegang_fase1 import request, paginas


async def fetch(application, path, accept='text/html', method='GET', encoding=None):
    messages = []
    async def receive():
        return {'type': 'http.request', 'body': b'', 'more_body': False}
    async def send(message):
        messages.append(message)
    try:
        await application({
            'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1',
            'method': method, 'scheme': 'http', 'path': path, 'raw_path': path.encode(),
            'query_string': b'', 'root_path': '', 'server': ('testserver', 80),
            'client': ('127.0.0.1', 1234), 'headers': [(b'host', b'testserver'), (b'accept', accept.encode())] + ([(b'accept-encoding', encoding.encode())] if encoding else []),
        }, receive, send)
    except RuntimeError:
        # ASGI herwerpt een ongehanteerde fout nadat het veilige 500-antwoord is gestuurd.
        if not messages:
            raise
    start = next(m for m in messages if m['type'] == 'http.response.start')
    body = b''.join(m.get('body', b'') for m in messages if m['type'] == 'http.response.body')
    return start['status'], dict(start['headers']), body


class Fase4Tests(unittest.TestCase):
    def setUp(self):
        with patch.dict(os.environ, {'WESPI_ENV': 'production'}):
            self.production = create_app()
        with patch.dict(os.environ, {'WESPI_ENV': 'staging'}):
            self.staging = create_app()

    def get(self, path, app=None, **kwargs):
        return asyncio.run(fetch(app or self.production, path, **kwargs))

    def test_public_seo_and_social_metadata(self):
        titles, descriptions = set(), set()
        for path in PUBLIC_PAGES:
            with self.subTest(path=path):
                status, headers, body = self.get(path)
                html = body.decode()
                self.assertEqual(status, 200)
                title = ' '.join(re.search(r'<title>(.*?)</title>', html, re.S).group(1).split())
                self.assertNotIn(title, titles)
                titles.add(title)
                tags = Markup(html).tags
                metas = {a.get('name', a.get('property')): a.get('content') for t, a in tags if t == 'meta'}
                self.assertTrue(metas['description'].strip())
                self.assertNotIn(metas['description'].strip(), descriptions)
                descriptions.add(metas['description'].strip())
                self.assertEqual(metas['og:url'], SITE_URL + path)
                self.assertEqual(metas['og:title'], title.replace('&amp;', '&'))
                self.assertTrue(Path(unquote(urlsplit(metas['og:image']).path).lstrip('/')).is_file())
                self.assertEqual([a['href'] for t, a in tags if t == 'link' and a.get('rel') == 'canonical'], [SITE_URL + path])
                self.assertEqual(sum(t == 'h1' for t, _ in tags), 1)
                self.assertNotIn(b'x-robots-tag', headers)
                self.assertFalse('noindex' in metas.get('robots', ''))
                self.assertTrue(all('alt' in a for t, a in tags if t == 'img'))
                self.assertIn('id="hoofdinhoud"', html)

    def test_sitemap_matches_only_approved_pages(self):
        status, headers, body = self.get('/sitemap.xml')
        self.assertEqual(status, 200)
        self.assertIn(b'application/xml', headers[b'content-type'])
        xml = ElementTree.fromstring(body)
        locations = [e.text for e in xml.findall('{*}url/{*}loc')]
        self.assertEqual(set(locations), {SITE_URL + path for path in PUBLIC_PAGES})
        self.assertEqual(len(locations), len(set(locations)))
        for url in locations:
            self.assertEqual(self.get(urlsplit(url).path)[0], 200)
        self.assertIn(SITE_URL + '/beeldbewerking', locations)
        self.assertEqual(len(locations), 16)
        self.assertNotIn(SITE_URL + '/slimmer-werken-v2', locations)

    def test_staging_and_production_robots(self):
        self.assertIn(b'Allow: /', self.get('/robots.txt')[2])
        self.assertIn(b'Sitemap: https://www.wespi.nl/sitemap.xml', self.get('/robots.txt')[2])
        self.assertIn(b'Disallow: /', self.get('/robots.txt', self.staging)[2])
        for path in ['/', '/contact', '/sitemap.xml', '/static/css/basis.css']:
            self.assertEqual(self.get(path, self.staging)[1][b'x-robots-tag'], b'noindex, nofollow')

    def test_404_content_negotiation_and_api_status(self):
        status, headers, body = self.get('/niet-bestaande-pagina')
        self.assertEqual(status, 404)
        self.assertIn(b'text/html', headers[b'content-type'])
        self.assertIn(b'href="/contact"', body)
        self.assertIn(b'noindex', body)
        self.assertEqual(headers[b'cache-control'], b'no-store')
        for path, accept in [('/api/ontbreekt', 'text/html'), ('/niet-bestaand', 'application/json'), ('/static/ontbreekt.css', 'text/html')]:
            status, headers, body = self.get(path, accept=accept)
            self.assertEqual(status, 404)
            self.assertIn(b'application/json', headers[b'content-type'])
            self.assertEqual(json.loads(body)['detail'], 'Not Found')
        self.assertEqual(self.get('/contact', method='DELETE')[0], 405)

    def test_safe_500_and_disabled_debug_docs(self):
        @self.production.get('/test-fout')
        def error():
            raise RuntimeError('GEHEIME_TESTWAARDE')
        for accept in ['text/html', 'application/json']:
            status, headers, body = self.get('/test-fout', accept=accept)
            self.assertEqual(status, 500)
            self.assertNotIn(b'GEHEIME_TESTWAARDE', body)
            self.assertEqual(headers[b'cache-control'], b'no-store')
            self.assertEqual(headers[b'x-content-type-options'], b'nosniff')
        self.assertFalse(self.production.debug)
        for path in ['/docs', '/redoc', '/openapi.json']:
            self.assertEqual(self.get(path)[0], 404)

    def test_security_cache_and_static_metadata(self):
        for path in ['/', '/contact', '/offerte', '/niet-bestaand', '/static/css/basis.css']:
            _, headers, _ = self.get(path)
            self.assertEqual(headers[b'x-content-type-options'], b'nosniff')
            self.assertEqual(headers[b'x-frame-options'], b'SAMEORIGIN')
            self.assertIn(b'strict-origin', headers[b'referrer-policy'])
        self.assertEqual(self.get('/')[1][b'cache-control'], b'no-cache')
        self.assertEqual(self.get('/contact')[1][b'cache-control'], b'no-store')
        self.assertEqual(self.get('/offerte')[1][b'cache-control'], b'no-store')
        headers = self.get('/static/css/basis.css')[1]
        self.assertIn(b'max-age=3600', headers[b'cache-control'])
        self.assertIn(b'etag', headers)

    def test_redirects_are_single_hop(self):
        for old, new in [('/beeldbewerking/auto', '/beeldbewerking/automotive'), ('/terms', '/algemene-voorwaarden'), ('/privacystatement', '/privacyverklaring')]:
            status, headers, _ = self.get(old)
            self.assertEqual(status, 301)
            self.assertEqual(headers[b'location'].decode(), new)
            self.assertEqual(self.get(new)[0], 200)

    def test_seo_migration_redirects_and_slash_variants(self):
        destinations = {
            '/productfotografie': SITE_URL + '/beeld',
            '/productfotografie/plattefotografie': SITE_URL + '/productfotografie/kledingfotografie#platte-fotografie',
            '/beeldbewerking/auto/voorbeelden': SITE_URL + '/beeldbewerking/automotive#achtergronden',
            '/overons': SITE_URL + '/over-wespi',
            '/contactus': SITE_URL + '/contact',
            '/diensten': SITE_URL + '/#diensten',
            '/diensten/contentbeheer': SITE_URL + '/data/productdata',
            '/studio': SITE_URL + '/productfotografie/kledingfotografie',
            '/beeldbewerking/auto': '/beeldbewerking/automotive',
            '/terms': '/algemene-voorwaarden',
            '/privacystatement': '/privacyverklaring',
        }
        for old, destination in destinations.items():
            for variant in (old, old + '/'):
                with self.subTest(path=variant):
                    status, headers, _ = self.get(variant)
                    self.assertEqual(status, 301)
                    self.assertEqual(headers[b'location'].decode(), destination)
                    target = urlsplit(destination)
                    status, headers, body = self.get(target.path)
                    self.assertEqual(status, 200)
                    self.assertNotIn(b'location', headers)
                    if target.fragment:
                        self.assertIn('id="' + target.fragment + '"', body.decode())

    def test_retired_odoo_urls_are_not_redirected(self):
        for path in ['/diensten/rendering', '/vriendenprijs', '/vriendenprijsaanvraag',
                     '/inontwikkeling', '/shop', '/shop/cart', '/appointment', '/calendar']:
            for variant in (path, path + '/'):
                with self.subTest(path=variant):
                    status, headers, _ = self.get(variant)
                    self.assertEqual(status, 404)
                    self.assertNotIn(b'location', headers)

    def test_migration_keeps_existing_service_urls(self):
        for path in ['/productfotografie/kledingfotografie', '/productfotografie/packshotfotografie',
                     '/productfotografie/kledingfotografie/ai-modelfotografie', '/beeldbewerking',
                     '/beeldbewerking/product', '/beeldbewerking/kleding', '/beeldbewerking/automotive']:
            with self.subTest(path=path):
                status, headers, _ = self.get(path)
                self.assertEqual(status, 200)
                self.assertNotIn(b'location', headers)

    def test_migration_preserves_query_before_fragment(self):
        status, headers, _ = asyncio.run(request('/productfotografie/plattefotografie/?utm_source=test'))
        self.assertEqual(status, 301)
        self.assertEqual(headers[b'location'].decode(), SITE_URL +
                         '/productfotografie/kledingfotografie?utm_source=test#platte-fotografie')

    def test_important_heroes_are_not_lazy_loaded(self):
        for path in ['/over-wespi', '/beeldbewerking/kleding']:
            tags = Markup(self.get(path)[2].decode()).tags
            first = next(a for t, a in tags if t == 'img' and 'logo' not in a.get('src', ''))
            self.assertNotEqual(first.get('loading'), 'lazy')
            self.assertEqual(first['fetchpriority'], 'high')

    def test_environment_fails_on_typo(self):
        with patch.dict(os.environ, {'WESPI_ENV': 'produciton'}):
            with self.assertRaises(ValueError):
                create_app()

    def test_page_compression_preserves_body_and_skips_media_forms(self):
        _, headers, compressed = self.get('/', encoding='gzip')
        self.assertEqual(headers[b'content-encoding'], b'gzip')
        self.assertIn(b'Accept-Encoding', headers[b'vary'])
        self.assertEqual(gzip.decompress(compressed), self.get('/')[2])
        for path in ['/contact', '/offerte', '/static/images/logo/wespi-logo.png']:
            self.assertNotIn(b'content-encoding', self.get(path, encoding='gzip')[1])

    def test_no_sensitive_smtp_exception_in_application_log(self):
        data = {'naam': 'Test', 'email': 'test@example.invalid', 'onderwerp': 'Vraag',
                'bericht': 'Vertrouwelijke inhoud', 'privacy_toestemming': 'accepted'}
        with patch.dict(os.environ, {'SMTP_HOST': 'smtp.example.invalid', 'SMTP_FROM': 'website@example.invalid',
                                    'SMTP_USERNAME': '', 'SMTP_PASSWORD': ''}), \
                patch.object(paginas, '_send_contact_email', side_effect=smtplib.SMTPException('GEHEIME_SMTP_WAARDE')), \
                self.assertLogs(paginas.logger, level='ERROR') as logs:
            self.assertEqual(asyncio.run(request('/contact', data))[0], 503)
        self.assertNotIn('GEHEIME_SMTP_WAARDE', '\n'.join(logs.output))
        self.assertTrue(all(record.exc_info is None for record in logs.records))

    def test_unfinished_and_test_routes_keep_existing_status(self):
        self.assertEqual(self.get('/beeldbewerking')[0], 200)
        self.assertNotIn(b'x-robots-tag', self.get('/beeldbewerking')[1])
        self.assertEqual(self.get('/beeldbewerking/product')[0], 200)
        status, _, body = self.get('/slimmer-werken-v2')
        self.assertEqual(status, 200)
        self.assertIn(b'noindex, nofollow', body)

    def test_active_internal_links_and_fragments(self):
        pages = {path: Markup(self.get(path)[2].decode()) for path in PUBLIC_PAGES}
        for path, markup in list(pages.items()):
            for tag, attrs in markup.tags:
                if tag != 'a':
                    continue
                href = attrs.get('href', '')
                self.assertTrue(href, path)
                url = urlsplit(href)
                if url.scheme in {'mailto', 'tel'} or url.netloc and url.netloc not in {'www.wespi.nl', 'testserver'}:
                    continue
                dest = url.path or path
                if dest.startswith('/static/'):
                    self.assertTrue(Path(unquote(dest).lstrip('/')).exists(), href)
                    continue
                if not dest.startswith('/'):
                    continue
                if dest not in pages:
                    status, _, body = self.get(dest)
                    self.assertEqual(status, 200, href)
                    pages[dest] = Markup(body.decode())
                if url.fragment:
                    self.assertTrue(any(a.get('id') == unquote(url.fragment) for _, a in pages[dest].tags), (path, href))
