from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
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
        "web": "Web",
    }

    geselecteerde_dienst = diensten.get(
        dienst,
        "",
    )

    return templates.TemplateResponse(
        request=request,
        name="offerte.html",
        context={
            "actieve_pagina": "offerte",
            "diensten": diensten,
            "dienst_code": dienst or "",
            "geselecteerde_dienst": geselecteerde_dienst,
        },
    )