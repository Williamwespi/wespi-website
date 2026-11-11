"""Bevestigde publieke URL's en lokaal toetsbare publicatie-instellingen."""
import os

SITE_URL = "https://www.wespi.nl"

# Alleen afgeronde pagina's. Dit verandert geen routes of navigatie.
PUBLIC_PAGES = {
    "/": "images/home/hero-kleding.png",
    "/beeld": "images/beeld/hero-beeld-productfotografie-wespi.png",
    "/beeldbewerking": "images/beeldbewerking/beeldbewerking-hero.png",
    "/productfotografie/kledingfotografie": "images/kledingfotografie/kledingfotografie-detail-gebreide-trui-wespi.jpg",
    "/productfotografie/kledingfotografie/ai-modelfotografie": "images/kledingfotografie/ai-modelfotografie/ai-modelfotografie-hero.jpg",
    "/productfotografie/packshotfotografie": "images/packshotfotografie/packshotfotografie-detail-accessoire.png",
    "/beeldbewerking/product": "images/beeldbewerking/product/productbeeldbewerking-horloge-groen-na-960.webp",
    "/beeldbewerking/kleding": "images/beeldbewerking/kleding/productfoto-kleding-1.jpg",
    "/beeldbewerking/automotive": "images/beeldbewerking/beeldbewerking/automotive/achtergronden/auto-geel-extra-achtergrond-3.jpg",
    "/data/productdata": "images/productdata/productdata-hero.png",
    "/slimmer-werken": "images/slimmer-werken/slimmer-werken-hero.png",
    "/over-wespi": "images/over-wespi/wespi-vlag.jpg",
    "/contact": "images/contact/contact-hero.png",
    "/offerte": "images/logo/wespi-logo.png",
    "/privacyverklaring": "images/logo/wespi-logo.png",
    "/algemene-voorwaarden": "images/logo/wespi-logo.png",
}


def environment():
    value = os.getenv("WESPI_ENV", "development").strip().lower()
    if value not in {"development", "staging", "production"}:
        raise ValueError("WESPI_ENV moet development, staging of production zijn.")
    return value


def social_context(request):
    image = PUBLIC_PAGES.get(request.url.path)
    return {
        "social_url": SITE_URL + request.url.path if image else None,
        "social_image": SITE_URL + "/static/" + image if image else None,
    }
