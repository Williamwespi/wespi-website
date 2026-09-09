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