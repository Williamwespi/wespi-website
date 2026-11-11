import json
import logging
import os
import re
import smtplib
import ssl
from dataclasses import dataclass
from email.message import EmailMessage
from pathlib import Path

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from siteconfig import SITE_URL


router = APIRouter()
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger(__name__)

# Voorlopige verkoopprijzen, exclusief btw; uitsluitend voor AI-modelfotografie.
AI_MODELFOTOGRAFIE_TARIEVEN = (
    {"titel": "1 AI-modelfoto", "prijs": "9,99", "omschrijving": "Eén modelbeeld van jouw kledingartikel."},
    {"titel": "3 AI-modelfoto’s", "prijs": "24,99", "omschrijving": "Drie beelden van hetzelfde kledingartikel."},
    {"titel": "AI-video", "prijs": "19,99", "omschrijving": "Een video van circa 10 seconden."},
    {"titel": "Combinatiepakket", "prijs": "39,99", "omschrijving": "3 foto's en 1 video van hetzelfde kledingartikel."},
)


def _ai_media_path(filename: str) -> str | None:
    relative = Path("images/kledingfotografie/ai-modelfotografie") / filename
    if (Path(__file__).resolve().parent.parent / "static" / relative).is_file():
        return relative.as_posix()
    return None


@router.get(
    "/productfotografie/kledingfotografie/ai-modelfotografie",
    response_class=HTMLResponse,
)
def ai_modelfotografie(request: Request):
    voorbeelden = json.loads(
        Path(__file__).with_name("ai_modellen.json").read_text(encoding="utf-8")
    )
    return templates.TemplateResponse(
        request=request,
        name="ai-modelfotografie.html",
        context={
            "actieve_pagina": "kledingfotografie",
            "hero": _ai_media_path("ai-modelfotografie-hero.jpg"),
            "voorbeelden": voorbeelden,
            "tarieven": AI_MODELFOTOGRAFIE_TARIEVEN,
        },
    )


@dataclass(frozen=True)
class SMTPConfiguration:
    host: str
    port: int
    sender: str
    username: str
    password: str


def _smtp_configuration() -> SMTPConfiguration | None:
    host = os.getenv("SMTP_HOST", "").strip()
    sender = os.getenv("SMTP_FROM", "").strip()
    username = os.getenv("SMTP_USERNAME", "").strip()
    password = os.getenv("SMTP_PASSWORD", "")

    if not host or not sender or bool(username) != bool(password):
        logger.error(
            "Formulier kan niet verzenden: SMTP_HOST en SMTP_FROM "
            "zijn vereist en SMTP_USERNAME/SMTP_PASSWORD moeten samen zijn ingesteld."
        )
        return None

    try:
        port = int(os.getenv("SMTP_PORT", "587"))
    except ValueError:
        logger.error("Formulier kan niet verzenden: SMTP_PORT is ongeldig.")
        return None

    if not 1 <= port <= 65535:
        logger.error("Formulier kan niet verzenden: SMTP_PORT is ongeldig.")
        return None

    return SMTPConfiguration(
        host=host,
        port=port,
        sender=sender,
        username=username,
        password=password,
    )


def _send_contact_email(
    form_data: dict[str, str],
    configuration: SMTPConfiguration,
) -> None:
    message = EmailMessage()
    message["Subject"] = f"Contactformulier: {form_data['onderwerp']}"
    message["From"] = configuration.sender
    message["To"] = "info@wespi.nl"
    message["Reply-To"] = form_data["email"]
    message.set_content(
        "\n".join(
            (
                f"Naam: {form_data['naam']}",
                f"Bedrijf: {form_data['bedrijfsnaam'] or '-'}",
                f"E-mailadres: {form_data['email']}",
                f"Telefoonnummer: {form_data['telefoonnummer'] or '-'}",
                f"Onderwerp: {form_data['onderwerp']}",
                "",
                "Bericht:",
                form_data["bericht"],
                "",
                "Privacytoestemming: gegeven",
            )
        )
    )

    _send_email(message, configuration)


def _send_email(message: EmailMessage, configuration: SMTPConfiguration) -> None:
    tls_context = ssl.create_default_context()
    implicit_tls = configuration.port == 465
    connection = (
        smtplib.SMTP_SSL(configuration.host, configuration.port, timeout=15, context=tls_context)
        if implicit_tls else
        smtplib.SMTP(configuration.host, configuration.port, timeout=15)
    )
    with connection as server:
        server.ehlo()
        if not implicit_tls:
            server.starttls(context=tls_context)
            server.ehlo()
        if configuration.username:
            server.login(configuration.username, configuration.password)
        refused_recipients = server.send_message(message)
        if refused_recipients:
            raise smtplib.SMTPRecipientsRefused(refused_recipients)


@router.get(
    "/",
    response_class=HTMLResponse,
)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "actieve_pagina": "home",
        },
    )


@router.get(
    "/beeld",
    response_class=HTMLResponse,
)
def beeld(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="beeld.html",
        context={
            "actieve_pagina": "beeld",
        },
    )


@router.get(
    "/productfotografie/kledingfotografie",
    response_class=HTMLResponse,
)
def kledingfotografie(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="kledingfotografie.html",
        context={
            "actieve_pagina": "kledingfotografie",
        },
    )


@router.get(
    "/productfotografie/packshotfotografie",
    response_class=HTMLResponse,
)
def packshotfotografie(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="packshotfotografie.html",
        context={
            "actieve_pagina": "packshotfotografie",
        },
    )


@router.get(
    "/beeldbewerking",
    response_class=HTMLResponse,
)
def beeldbewerking(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="beeldbewerking.html",
        context={
            "actieve_pagina": "beeldbewerking",
        },
    )


@router.get("/beeldbewerking/product", response_class=HTMLResponse)
def productbeeldbewerking(request: Request):
    return templates.TemplateResponse(
        request=request, name="productbeeldbewerking.html",
        context={"actieve_pagina": "beeldbewerking"},
    )


@router.get(
    "/beeldbewerking/kleding",
    response_class=HTMLResponse,
)
def kledingbeeldbewerking(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="kledingbeeldbewerking.html",
        context={"actieve_pagina": "beeldbewerking"},
    )


@router.get(
    "/beeldbewerking/automotive",
    response_class=HTMLResponse,
)
def automotive(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="automotive.html",
        context={"actieve_pagina": "beeldbewerking"},
    )


@router.get(
    "/data/productdata",
    response_class=HTMLResponse,
)
def productdata(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="productdata.html",
        context={
            "actieve_pagina": "data",
        },
    )




@router.get(
    "/slimmer-werken",
    response_class=HTMLResponse,
)
def slimmer_werken(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="slimmer-werken.html",
        context={
            "actieve_pagina": "slimmer-werken",
        },
    )


@router.get(
    "/slimmer-werken-v2",
    response_class=HTMLResponse,
)
def slimmer_werken_v2(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="slimmer-werken-v2.html",
        context={
            "actieve_pagina": "slimmer-werken-v2",
            "applicaties": [],
        },
    )


@router.get(
    "/offerte",
    response_class=HTMLResponse,
)
def offerte(
    request: Request,
    dienst: str | None = None,
):
    return _offerte_response(request, {"Dienst": OFFERTE_DIENSTEN.get(dienst, "")})


OFFERTE_DIENSTEN = {
    "kledingfotografie": "Kledingfotografie",
    "packshotfotografie": "Packshotfotografie",
    "beeldbewerking": "Beeldbewerking",
    "data": "Productdata",
    "slimmer-werken": "Slimmer werken",
}
OFFERTE_FOTOGRAFIE = ("", "Bodyform", "Platte fotografie", "Combinatie")


def _offerte_response(
    request: Request,
    form_data: dict[str, str],
    errors: dict[str, str] | None = None,
    status: str = "",
    success: bool = False,
    code: int = 200,
):
    return templates.TemplateResponse(
        request=request,
        name="oferte.html",
        context={
            "actieve_pagina": "offerte",
            "diensten": OFFERTE_DIENSTEN,
            "geselecteerde_dienst": form_data.get("Dienst", ""),
            "form_data": form_data,
            "form_errors": errors or {},
            "form_status": status,
            "form_success": success,
        },
        status_code=code,
    )


def _send_offerte_email(
    form_data: dict[str, str], configuration: SMTPConfiguration,
) -> None:
    message = EmailMessage()
    message["Subject"] = "Nieuwe offerteaanvraag via Wespi"
    message["From"] = configuration.sender
    message["To"] = "info@wespi.nl"
    message["Reply-To"] = form_data["E-mail"]
    message.set_content("\n".join(
        f"{field}: {value or '-'}" for field, value in form_data.items()
    ))
    _send_email(message, configuration)


@router.post("/offerte", response_class=HTMLResponse)
def offerte_versturen(
    request: Request,
    naam: str = Form(default="", alias="Naam"),
    bedrijf: str = Form(default="", alias="Bedrijfsnaam"),
    email: str = Form(default="", alias="E-mail"),
    telefoon: str = Form(default="", alias="Telefoon"),
    dienst: str = Form(default="", alias="Dienst"),
    aantal: str = Form(default="", alias="Aantal artikelen"),
    fotografie: str = Form(default="", alias="Type kledingfotografie"),
    toelichting: str = Form(default="", alias="Toelichting"),
    website: str = Form(default=""),
):
    form_data = {
        "Naam": naam.strip(),
        "Bedrijfsnaam": bedrijf.strip(),
        "E-mail": email.strip(),
        "Telefoon": telefoon.strip(),
        "Dienst": dienst.strip(),
        "Aantal artikelen": aantal.strip(),
        "Type kledingfotografie": fotografie.strip(),
        "Toelichting": toelichting.strip(),
    }
    if website.strip():
        return _offerte_response(
            request, {}, code=400,
            status="De aanvraag kon niet worden verwerkt. Probeer het later opnieuw.",
        )

    errors = {}
    for field in ("Naam", "E-mail", "Dienst", "Toelichting"):
        if not form_data[field]:
            errors[field] = "Vul dit verplichte veld in."
    limits = {
        "Naam": 120, "Bedrijfsnaam": 160, "E-mail": 254, "Telefoon": 40,
        "Dienst": 80, "Aantal artikelen": 120, "Type kledingfotografie": 80,
        "Toelichting": 5000,
    }
    for field, value in form_data.items():
        if len(value) > limits[field]:
            errors[field] = "Deze invoer is te lang."
        if field != "Toelichting" and any(
            ord(char) < 32 or ord(char) == 127 for char in value
        ):
            errors[field] = "Gebruik geen regeleinden of controletekens."
    if form_data["E-mail"] and not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+", form_data["E-mail"],
    ):
        errors["E-mail"] = "Vul een geldig e-mailadres in."
    if form_data["Dienst"] not in OFFERTE_DIENSTEN.values():
        errors["Dienst"] = "Kies een dienst uit de lijst."
    if form_data["Type kledingfotografie"] not in OFFERTE_FOTOGRAFIE:
        errors["Type kledingfotografie"] = "Kies een fotografietype uit de lijst."
    if errors:
        return _offerte_response(
            request, form_data, errors, "Controleer de gemarkeerde velden.", code=422,
        )

    configuration = _smtp_configuration()
    if configuration is None:
        return _offerte_response(
            request, form_data, code=503,
            status=("Het offerteformulier is op dit moment niet beschikbaar. "
                    "Neem rechtstreeks contact op via info@wespi.nl."),
        )
    try:
        _send_offerte_email(form_data, configuration)
    except (OSError, ValueError, smtplib.SMTPException):
        logger.error("Verzenden van de offerteaanvraag is mislukt.")
        return _offerte_response(
            request, form_data, code=503,
            status=("De aanvraag is niet verzonden. Probeer het later opnieuw "
                    "of neem rechtstreeks contact op via info@wespi.nl."),
        )
    return _offerte_response(
        request, {}, success=True,
        status=("Bedankt! Je offerteaanvraag is verzonden. "
                "We nemen zo snel mogelijk contact met je op."),
    )


SEO_MIGRATIE_REDIRECTS = {
    "/productfotografie": "/beeld",
    "/productfotografie/plattefotografie": "/productfotografie/kledingfotografie#platte-fotografie",
    "/beeldbewerking/auto/voorbeelden": "/beeldbewerking/automotive#achtergronden",
    "/overons": "/over-wespi",
    "/contactus": "/contact",
    "/diensten": "/#diensten",
    "/diensten/contentbeheer": "/data/productdata",
    "/studio": "/productfotografie/kledingfotografie",
}


def oude_odoo_route(request: Request):
    destination = SITE_URL + SEO_MIGRATIE_REDIRECTS[request.url.path.rstrip("/")]
    path, separator, fragment = destination.partition("#")
    if request.url.query:
        path += "?" + request.url.query
    return RedirectResponse(path + (separator + fragment if separator else ""), status_code=301)


for oud_pad in SEO_MIGRATIE_REDIRECTS:
    for variant in (oud_pad, oud_pad + "/"):
        router.add_api_route(variant, oude_odoo_route, methods=["GET", "HEAD"], include_in_schema=False)


@router.get("/beeldbewerking/auto/", include_in_schema=False)
@router.get("/beeldbewerking/auto", include_in_schema=False)
def oude_auto_route():
    return RedirectResponse("/beeldbewerking/automotive", status_code=301)


@router.get("/terms/", include_in_schema=False)
@router.get("/terms", include_in_schema=False)
def oude_voorwaarden_route():
    return RedirectResponse("/algemene-voorwaarden", status_code=301)


@router.get("/privacystatement/", include_in_schema=False)
@router.get("/privacystatement", include_in_schema=False)
def oude_privacy_route():
    return RedirectResponse("/privacyverklaring", status_code=301)


@router.get(
    "/contact",
    response_class=HTMLResponse,
)
def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={
            "actieve_pagina": "contact",
            "form_data": {},
            "form_errors": {},
            "form_status": "",
        },
    )


@router.post(
    "/contact",
    response_class=HTMLResponse,
)
def contact_versturen(
    request: Request,
    naam: str = Form(default=""),
    bedrijfsnaam: str = Form(default=""),
    email: str = Form(default=""),
    telefoonnummer: str = Form(default=""),
    onderwerp: str = Form(default=""),
    bericht: str = Form(default=""),
    privacy_toestemming: str = Form(default=""),
    website: str = Form(default=""),
):
    form_data = {
        "naam": naam.strip(),
        "bedrijfsnaam": bedrijfsnaam.strip(),
        "email": email.strip(),
        "telefoonnummer": telefoonnummer.strip(),
        "onderwerp": onderwerp.strip(),
        "bericht": bericht.strip(),
    }

    if website.strip():
        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context={
                "actieve_pagina": "contact",
                "form_data": {},
                "form_errors": {},
                "form_status": (
                    "Het bericht kon niet worden verwerkt. Probeer het later opnieuw."
                ),
            },
            status_code=400,
        )

    form_errors: dict[str, str] = {}
    required_fields = {
        "naam": "Vul je naam in.",
        "email": "Vul je e-mailadres in.",
        "onderwerp": "Vul het onderwerp in.",
        "bericht": "Vul je bericht in.",
    }
    field_limits = {
        "naam": 120,
        "bedrijfsnaam": 160,
        "email": 254,
        "telefoonnummer": 40,
        "onderwerp": 180,
        "bericht": 5000,
    }

    for field, error in required_fields.items():
        if not form_data[field]:
            form_errors[field] = error

    for field, value in form_data.items():
        if len(value) > field_limits[field]:
            form_errors[field] = "Deze invoer is te lang."
        if field != "bericht" and any(
            ord(character) < 32 or ord(character) == 127
            for character in value
        ):
            form_errors[field] = "Gebruik geen regeleinden of controletekens."

    if form_data["email"] and not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+",
        form_data["email"],
    ):
        form_errors["email"] = "Vul een geldig e-mailadres in."

    if privacy_toestemming != "accepted":
        form_errors["privacy_toestemming"] = (
            "Geef toestemming voor het verwerken van je gegevens."
        )

    if form_errors:
        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context={
                "actieve_pagina": "contact",
                "form_data": form_data,
                "form_errors": form_errors,
                "form_status": "Controleer de gemarkeerde velden.",
                "privacy_accepted": privacy_toestemming == "accepted",
            },
            status_code=422,
        )

    configuration = _smtp_configuration()
    if configuration is None:
        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context={
                "actieve_pagina": "contact",
                "form_data": form_data,
                "form_errors": {},
                "form_status": (
                    "Het contactformulier is op dit moment niet beschikbaar. "
                    "Neem rechtstreeks contact op via info@wespi.nl."
                ),
                "privacy_accepted": privacy_toestemming == "accepted",
            },
            status_code=503,
        )

    try:
        _send_contact_email(form_data, configuration)
    except (OSError, ValueError, smtplib.SMTPException):
        logger.error("Verzenden van het contactformulier is mislukt.")
        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context={
                "actieve_pagina": "contact",
                "form_data": form_data,
                "form_errors": {},
                "form_status": (
                    "Het bericht is niet verzonden. Probeer het later opnieuw "
                    "of neem rechtstreeks contact op via info@wespi.nl."
                ),
                "privacy_accepted": privacy_toestemming == "accepted",
            },
            status_code=503,
        )

    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={
            "actieve_pagina": "contact",
            "form_data": {},
            "form_errors": {},
            "form_status": "Bedankt voor je bericht. We nemen zo snel mogelijk contact op.",
            "form_success": True,
        },
    )


@router.get("/privacyverklaring", response_class=HTMLResponse)
def privacyverklaring(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="privacyverklaring.html",
        context={"actieve_pagina": "privacyverklaring"},
    )


@router.get("/algemene-voorwaarden", response_class=HTMLResponse)
def algemene_voorwaarden(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="algemene-voorwaarden.html",
        context={"actieve_pagina": "algemene-voorwaarden"},
    )


@router.get(
    "/over-wespi",
    response_class=HTMLResponse,
)
def over_wespi(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="over-wespi.html",
        context={
            "actieve_pagina": "over-wespi",
        },
    )
