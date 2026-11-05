"""Gerichte ASGI-tests zonder externe mail of extra testdependencies.

Uitvoeren vanuit de projectmap: python -B -m unittest discover -s tests -v
"""
import asyncio
import importlib
import os
import smtplib
import unittest
from html.parser import HTMLParser
from unittest.mock import patch
from urllib.parse import urlencode, urlsplit

from app import app

paginas = importlib.import_module("routes.paginas")


async def request(path, data=None):
    url = urlsplit(path)
    body = urlencode(data or {}).encode()
    messages = []
    delivered = False

    async def receive():
        nonlocal delivered
        if not delivered:
            delivered = True
            return {"type": "http.request", "body": body, "more_body": False}
        return {"type": "http.disconnect"}

    async def send(message):
        messages.append(message)

    await app({
        "type": "http", "asgi": {"version": "3.0"}, "http_version": "1.1",
        "method": "POST" if data is not None else "GET", "scheme": "http",
        "path": url.path, "raw_path": url.path.encode(), "query_string": url.query.encode(),
        "root_path": "", "server": ("testserver", 80), "client": ("127.0.0.1", 1234),
        "headers": [(b"host", b"testserver"),
                    (b"content-type", b"application/x-www-form-urlencoded"),
                    (b"content-length", str(len(body)).encode())],
    }, receive, send)
    start = next(m for m in messages if m["type"] == "http.response.start")
    text = b"".join(m.get("body", b"") for m in messages if m["type"] == "http.response.body").decode()
    return start["status"], dict(start["headers"]), text


class Markup(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        self.tags.append((tag, dict(attributes)))


class Fase1Tests(unittest.TestCase):
    def setUp(self):
        self.env = patch.dict(os.environ, {
            "SMTP_HOST": "smtp.example.invalid", "SMTP_PORT": "587",
            "SMTP_FROM": "website@example.invalid", "SMTP_USERNAME": "test-user",
            "SMTP_PASSWORD": "dummy-test-only",
        })
        self.env.start()
        self.smtp_patch = patch.object(smtplib, "SMTP")
        self.smtp = self.smtp_patch.start()
        self.server = self.smtp.return_value.__enter__.return_value
        self.server.send_message.return_value = {}
        self.addCleanup(self.env.stop)
        self.addCleanup(self.smtp_patch.stop)
        self.quote = {
            "Naam": "Test Aanvrager", "Bedrijfsnaam": "Testbedrijf & Co",
            "E-mail": "bezoeker@example.invalid", "Telefoon": "0612345678",
            "Dienst": "Kledingfotografie", "Aantal artikelen": "Ongeveer 50",
            "Type kledingfotografie": "Bodyform", "Toelichting": "Eerste regel\nTweede regel: zomercollectie.",
        }
        self.contact = {
            "naam": "Test Aanvrager", "bedrijfsnaam": "Testbedrijf & Co",
            "email": "bezoeker@example.invalid", "telefoonnummer": "0612345678",
            "onderwerp": "Testvraag", "bericht": "Eerste regel\nTweede regel.",
            "privacy_toestemming": "accepted",
        }

    def fetch(self, path, data=None):
        return asyncio.run(request(path, data))

    def test_success_quote_all_fields_and_safe_headers(self):
        status, _, text = self.fetch("/offerte", self.quote)
        self.assertEqual(status, 200)
        self.assertIn("Je offerteaanvraag is verzonden", text)
        message = self.server.send_message.call_args.args[0]
        self.assertEqual(message["To"], "info@wespi.nl")
        self.assertEqual(message["From"], "website@example.invalid")
        self.assertEqual(message["Reply-To"], self.quote["E-mail"])
        self.assertEqual(message["Subject"], "Nieuwe offerteaanvraag via Wespi")
        for field, value in self.quote.items():
            self.assertIn(f"{field}: {value}", message.get_content())
        self.server.starttls.assert_called_once()
        tls_context = self.server.starttls.call_args.kwargs["context"]
        self.assertTrue(tls_context.check_hostname)
        self.server.login.assert_called_once_with("test-user", "dummy-test-only")
        self.smtp.assert_called_once_with("smtp.example.invalid", 587, timeout=15)
        self.assertEqual(self.server.ehlo.call_count, 2)

    def test_success_contact_headers_and_body(self):
        status, _, text = self.fetch("/contact", self.contact)
        self.assertEqual(status, 200)
        self.assertIn("Bedankt voor je bericht", text)
        message = self.server.send_message.call_args.args[0]
        self.assertEqual(message["To"], "info@wespi.nl")
        self.assertEqual(message["From"], "website@example.invalid")
        self.assertEqual(message["Reply-To"], self.contact["email"])
        self.assertEqual(message["Subject"], "Contactformulier: Testvraag")
        for key, value in self.contact.items():
            if key != "privacy_toestemming":
                self.assertIn(value, message.get_content())
        self.assertIn("Privacytoestemming: gegeven", message.get_content())

    def test_missing_required_fields(self):
        for path, data, fields in (
            ("/offerte", self.quote, ("Naam", "E-mail", "Dienst", "Toelichting")),
            ("/contact", self.contact, ("naam", "email", "onderwerp", "bericht", "privacy_toestemming")),
        ):
            for field in fields:
                with self.subTest(path=path, field=field):
                    invalid = {**data, field: ""}
                    self.assertEqual(self.fetch(path, invalid)[0], 422)
        self.smtp.assert_not_called()

    def test_invalid_input(self):
        cases = (
            ("/offerte", self.quote, "E-mail", "ongeldig"),
            ("/offerte", self.quote, "E-mail", "a@example.nl\r\nBcc: x@example.nl"),
            ("/offerte", self.quote, "Naam", "x\x00y"),
            ("/offerte", self.quote, "Toelichting", "x" * 5001),
            ("/offerte", self.quote, "Dienst", "Onbekende dienst"),
            ("/offerte", self.quote, "Type kledingfotografie", "Onbekend"),
            ("/contact", self.contact, "email", "ongeldig"),
            ("/contact", self.contact, "onderwerp", "Hoi\r\nBcc: x@example.nl"),
            ("/contact", self.contact, "bericht", "x" * 5001),
        )
        for path, data, field, value in cases:
            with self.subTest(path=path, field=field, value=value[:30]):
                self.assertEqual(self.fetch(path, {**data, field: value})[0], 422)
        self.smtp.assert_not_called()

    def test_honeypots(self):
        for path, data in (("/offerte", self.quote), ("/contact", self.contact)):
            self.assertEqual(self.fetch(path, {**data, "website": "spam"})[0], 400)
        self.smtp.assert_not_called()

    def test_invalid_smtp_configuration(self):
        for settings in ({"SMTP_HOST": ""}, {"SMTP_FROM": ""}, {"SMTP_PORT": "abc"},
                         {"SMTP_PORT": "0"}, {"SMTP_PORT": "65536"}, {"SMTP_PASSWORD": ""}):
            for path, data in (("/offerte", self.quote), ("/contact", self.contact)):
                with self.subTest(settings=settings, path=path), patch.dict(os.environ, settings), self.assertLogs("routes.paginas", level="ERROR"):
                    status, _, text = self.fetch(path, data)
                    self.assertEqual(status, 503)
                    self.assertIn("op dit moment niet beschikbaar", text)
        self.smtp.assert_not_called()

    def assert_values_retained(self, text, data):
        tags = Markup(text).tags
        inputs = {attrs.get("name"): attrs for tag, attrs in tags if tag == "input"}
        for name, value in data.items():
            if name in inputs:
                if name == "privacy_toestemming":
                    self.assertIn("checked", inputs[name])
                else:
                    self.assertEqual(inputs[name]["value"], value)
        if "Dienst" in data:
            selected = [a["value"] for t, a in tags if t == "option" and "selected" in a]
            self.assertIn(data["Dienst"], selected)
            self.assertIn(data["Type kledingfotografie"], selected)
        self.assertIn(data.get("Toelichting", data.get("bericht")), text)

    def test_failed_sending_preserves_fields(self):
        for failure in (OSError("offline"), smtplib.SMTPException("simulatie"), ValueError("simulatie")):
            self.server.send_message.side_effect = failure
            for path, data in (("/offerte", self.quote), ("/contact", self.contact)):
                with self.subTest(path=path, failure=type(failure).__name__):
                    with self.assertLogs("routes.paginas", level="ERROR"):
                        status, _, text = self.fetch(path, data)
                    self.assertEqual(status, 503)
                    self.assertIn("niet verzonden", text)
                    self.assert_values_retained(text, data)

    def test_missing_configuration_preserves_fields(self):
        with patch.dict(os.environ, {"SMTP_HOST": ""}), self.assertLogs("routes.paginas", level="ERROR"):
            for path, data in (("/offerte", self.quote), ("/contact", self.contact)):
                status, _, text = self.fetch(path, data)
                self.assertEqual(status, 503)
                self.assert_values_retained(text, data)

    def test_recipient_refusal_is_failure(self):
        self.server.send_message.return_value = {"info@wespi.nl": (550, b"refused")}
        for path, data in (("/offerte", self.quote), ("/contact", self.contact)):
            with self.assertLogs("routes.paginas", level="ERROR"):
                status, _, text = self.fetch(path, data)
            self.assertEqual(status, 503)
            self.assertNotIn('role="status"', text)

    def test_tls_and_login_failure(self):
        for step in ("starttls", "login"):
            method = getattr(self.server, step)
            method.side_effect = smtplib.SMTPException("simulatie")
            for path, data in (("/offerte", self.quote), ("/contact", self.contact)):
                with self.assertLogs("routes.paginas", level="ERROR"):
                    self.assertEqual(self.fetch(path, data)[0], 503)
            method.side_effect = None
        self.server.send_message.assert_not_called()

    def test_query_preselection(self):
        for code, name in paginas.OFFERTE_DIENSTEN.items():
            status, _, text = self.fetch("/offerte?dienst=" + code)
            self.assertEqual(status, 200)
            selected = [a["value"] for t, a in Markup(text).tags if t == "option" and "selected" in a]
            self.assertIn(name, selected)
        self.assertEqual(self.fetch("/offerte?dienst=onbekend")[0], 200)

    def test_optional_fields_and_escaping(self):
        minimal = {key: self.quote[key] for key in ("Naam", "E-mail", "Dienst", "Toelichting")}
        self.assertEqual(self.fetch("/offerte", minimal)[0], 200)
        invalid = {**self.quote, "Naam": '<script>alert("x")</script>', "E-mail": "ongeldig"}
        status, _, text = self.fetch("/offerte", invalid)
        self.assertEqual(status, 422)
        self.assertIn("&lt;script&gt;", text)
        self.assertNotIn('<script>alert("x")</script>', text)

    def test_redirects_and_destinations(self):
        for old, new in (("/beeldbewerking/auto", "/beeldbewerking/automotive"),
                         ("/terms", "/algemene-voorwaarden"), ("/privacystatement", "/privacyverklaring")):
            status, headers, _ = self.fetch(old)
            self.assertEqual(status, 301)
            self.assertEqual(headers[b"location"].decode(), new)
            self.assertEqual(self.fetch(new)[0], 200)

    def test_existing_routes_footer_and_navigation_links(self):
        paths = [r.path for r in paginas.router.routes if "GET" in getattr(r, "methods", ())
                 and getattr(r, "response_class", None) is paginas.HTMLResponse]
        self.assertEqual(len(paths), 16)
        cache = {path: self.fetch(path) for path in paths}
        for path, (status, _, text) in cache.items():
            with self.subTest(path=path):
                self.assertEqual(status, 200)
                footer = text.split('<footer class="site-footer">')[1].split("</footer>")[0]
                self.assertNotIn('href="#"', footer)
                self.assertIn('href="/contact"', footer)
                self.assertIn('href="/over-wespi"', footer)
                for tag, attrs in Markup(footer).tags:
                    href = attrs.get("href", "")
                    if tag == "a" and href.startswith("/"):
                        target = urlsplit(href)
                        self.assertIn(target.path, cache)
                        if target.fragment:
                            self.assertIn(f'id="{target.fragment}"', cache[target.path][2])
                # Header remains structurally unchanged; verify its existing local destinations.
                header = text.split("</header>")[0]
                for tag, attrs in Markup(header).tags:
                    href = attrs.get("href", "")
                    if tag == "a" and href.startswith("/"):
                        target = urlsplit(href)
                        self.assertIn(target.path, cache)
                        if target.fragment:
                            self.assertIn(f'id="{target.fragment}"', cache[target.path][2])

    def test_bodyform_and_privacy_links(self):
        text = self.fetch("/productfotografie/kledingfotografie")[2]
        self.assertIn('href="#bodyform"', text)
        self.assertIn('id="bodyform"', text)
        text = self.fetch("/privacyverklaring")[2]
        self.assertNotIn("7122 LX", text)
        self.assertIn("7122 LC", text)
        self.assertNotIn("https://info@wespi.nl", text)
        self.assertNotIn("https://william@wespi.nl", text)
        self.assertIn('href="mailto:info@wespi.nl"', text)
        self.assertIn('href="mailto:william@wespi.nl"', text)


if __name__ == "__main__":
    unittest.main()
