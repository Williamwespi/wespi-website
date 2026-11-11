"""Regressies voor beeldvarianten, prijsvermeldingen en CTA-selectie."""
import asyncio
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

from test_livegang_fase1 import Markup, paginas, request


class Fase3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {}
        for route in paginas.router.routes:
            if "GET" in route.methods and route.response_class is paginas.HTMLResponse:
                status, _, html = asyncio.run(request(route.path))
                cls.pages[route.path] = (status, html)

    def test_doctype_and_all_page_responses(self):
        for path, (status, html) in self.pages.items():
            with self.subTest(path=path):
                self.assertEqual(status, 200)
                # Een BOM na uitvoer van een template-import veroorzaakt quirksmode.
                self.assertTrue(html.removeprefix("\ufeff").startswith("<!DOCTYPE html>"))
                self.assertNotIn("{{ beeld", html)

    def test_rendered_static_assets_exist(self):
        for path, (_, html) in self.pages.items():
            for tag, attrs in Markup(html).tags:
                urls = [attrs.get(key, "") for key in ("src", "poster", "data-lightbox-src")]
                if tag == "link" and attrs.get("rel") == "stylesheet":
                    urls.append(attrs.get("href", ""))
                urls.extend(candidate.strip().split()[0] for candidate in attrs.get("srcset", "").split(",") if candidate.strip())
                for url in urls:
                    filename = unquote(urlsplit(url).path)
                    if filename.startswith("/static/"):
                        with self.subTest(path=path, asset=filename):
                            self.assertTrue(Path(filename.lstrip("/")).is_file())

    def test_media_register_preserves_originals_and_zoom_sources(self):
        media = paginas.templates.env.get_template("onderdelen/beeldvarianten.html").module.beelden
        self.assertGreaterEqual(len(media), 60)
        for original, data in media.items():
            with self.subTest(original=original):
                self.assertTrue((Path("static") / original).is_file())
                self.assertTrue((Path("static") / data["zoom"]).is_file())
                for filename in [data["full"], *(p for p, _ in data["variants"])]:
                    with (Path("static") / filename).open("rb") as file:
                        header = file.read(12)
                    self.assertEqual(header[:4], b"RIFF")
                    self.assertEqual(header[8:12], b"WEBP")
                self.assertTrue(all(width < data["width"] for _, width in data["variants"]))
        # De enige 16-bits PNG blijft voor vergroting in het oorspronkelijke formaat.
        original = "images/packshotfotografie/accessoirefotografie-zonnebril-wespi.png"
        self.assertEqual(media[original]["zoom"], original)

    def test_unknown_future_media_paths_fall_back(self):
        template = paginas.templates.env.from_string(
            "{% from 'onderdelen/beeldvarianten.html' import beeldpad %}"
            "{{ beeldpad('images/toekomstige-foto.jpg') }}"
        )
        self.assertEqual(template.render(), "images/toekomstige-foto.jpg")

    def test_contact_alternative_and_footer_remain(self):
        hidden = {"/contact", "/offerte"}
        for path, (_, html) in self.pages.items():
            with self.subTest(path=path):
                tags = Markup(html).tags
                general_ctas = [a for t, a in tags if t == "section" and a.get("class") == "cta"]
                self.assertEqual(len(general_ctas), 0 if path in hidden else 1)
                self.assertIn('<footer class="site-footer">', html)
                self.assertIn('href="/contact"', html)
                if path in {"/contact", "/offerte"}:
                    self.assertTrue(any(t == "form" and a.get("method") == "post" for t, a in tags))

    def test_confirmed_vat_and_existing_price_amounts(self):
        prices = {
            "/productfotografie/kledingfotografie": ("15,99", "3,49", "10,99", "2,49"),
            "/productfotografie/packshotfotografie": ("9,99", "2,99"),
            "/beeldbewerking/product": ("2,49",),
            "/slimmer-werken": ("249", "499"),
            "/data/productdata": ("0,49", "0,99", "1,99", "75", "99", "189", "299"),
        }
        for path, amounts in prices.items():
            html = self.pages[path][1]
            with self.subTest(path=path):
                self.assertIn('class="prijs-btw"', html)
                self.assertIn("exclusief btw", html)
                for amount in amounts:
                    self.assertRegex(html, r"€\s*" + re.escape(amount) + r"(?:\s|<|\.)")


if __name__ == "__main__":
    unittest.main()
