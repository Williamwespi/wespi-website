import logging
import os
import re
import smtplib
from dataclasses import dataclass
from email.message import EmailMessage

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger(__name__)


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
            "Contactformulier kan niet verzenden: SMTP_HOST en SMTP_FROM "
            "zijn vereist en SMTP_USERNAME/SMTP_PASSWORD moeten samen zijn ingesteld."
        )
        return None

    try:
        port = int(os.getenv("SMTP_PORT", "587"))
    except ValueError:
        logger.error("Contactformulier kan niet verzenden: SMTP_PORT is ongeldig.")
        return None

    if not 1 <= port <= 65535:
        logger.error("Contactformulier kan niet verzenden: SMTP_PORT is ongeldig.")
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

    with smtplib.SMTP(
        configuration.host,
        configuration.port,
        timeout=15,
    ) as server:
        server.ehlo()
        server.starttls()
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
    diensten = {
        "kledingfotografie": "Kledingfotografie",
        "packshotfotografie": "Packshotfotografie",
        "beeldbewerking": "Beeldbewerking",
        "data": "Productdata",
        "slimmer-werken": "Slimmer werken",
    }

    geselecteerde_dienst = diensten.get(
        dienst,
        "",
    )

    return templates.TemplateResponse(
        request=request,
        name="oferte.html",
        context={
            "actieve_pagina": "offerte",
            "diensten": diensten,
            "dienst_code": dienst or "",
            "geselecteerde_dienst": geselecteerde_dienst,
        },
    )


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
async def contact_versturen(
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
            },
            status_code=503,
        )

    try:
        _send_contact_email(form_data, configuration)
    except (OSError, ValueError, smtplib.SMTPException):
        logger.exception("Verzenden van het contactformulier is mislukt.")
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
