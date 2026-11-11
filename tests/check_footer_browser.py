"""Controle van de gedeelde afsluiting op alle publieke pagina's, lokaal in Chrome."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from siteconfig import PUBLIC_PAGES
from playwright.sync_api import sync_playwright

BASE = 'http://127.0.0.1:8765'
with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='chrome', headless=True)
    for width in [1440, 768, 375]:
        page = browser.new_page(viewport={'width': width, 'height': 900})
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
        page.on('response', lambda response: errors.append(f'{response.status}: {response.url}') if response.status >= 400 else None)
        for route in PUBLIC_PAGES:
            assert page.goto(BASE + route).status == 200, route
            assert page.locator('.site-footer').count() == 1, route
            assert page.locator('[id="contact"]').count() <= 1, route
            cta = page.locator('section.cta')
            if route in {'/contact', '/offerte'}:
                assert cta.count() == 0, route
                assert page.locator('form[method="post"]').is_visible(), route
            else:
                assert cta.count() == 1, route
                cta.scroll_into_view_if_needed()
                cta.locator('img').evaluate_all('(es)=>Promise.all(es.map(i=>i.decode()))')
                assert cta.is_visible(), route
                assert cta.locator('.sectie-bovenkop').inner_text() == 'SAMEN AAN DE SLAG?', route
                assert cta.locator('.cta-hoofdknop').is_visible(), route
                assert cta.locator('.cta-hoofdknop').get_attribute('href') == 'mailto:info@wespi.nl', route
                assert cta.evaluate('(e)=>e.clientHeight>400'), route
                assert cta.evaluate('(e)=>e.scrollWidth<=innerWidth'), route
            assert not errors, (width, route, errors)
        print(f'{width}px: gedeelde afsluiting op 13 publieke pagina\u2019s zichtbaar; Contact/Offerte behouden formulier; geen dubbele contact-ids of console-/HTTP-fouten.', flush=True)
        page.close()
    browser.close()
