from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, PlainTextResponse, Response
from starlette.exceptions import HTTPException
from starlette.middleware.gzip import GZipMiddleware

from routes.paginas import router as paginas_router, templates
from siteconfig import PUBLIC_PAGES, SITE_URL, environment, social_context


class ResponsePolicy:
    """Geen redirects/hostaannames; TLS wordt door de productieproxy beheerd."""
    def __init__(self, app, production):
        self.app = app
        self.production = production

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        async def policy_send(message):
            if message["type"] == "http.response.start":
                headers = list(message.get("headers", []))
                headers += [
                    (b"x-content-type-options", b"nosniff"),
                    (b"referrer-policy", b"strict-origin-when-cross-origin"),
                    (b"x-frame-options", b"SAMEORIGIN"),
                    (b"permissions-policy", b"camera=(), microphone=(), geolocation=()"),
                ]
                if not self.production:
                    headers.append((b"x-robots-tag", b"noindex, nofollow"))
                if scope["path"] in {"/contact", "/offerte"} or message["status"] >= 400:
                    cache = b"no-store"
                elif scope["path"].startswith("/static/"):
                    cache = b"public, max-age=3600"
                else:
                    cache = b"no-cache"
                headers.append((b"cache-control", cache))
                message = {**message, "headers": headers}
            await send(message)

        await self.app(scope, receive, policy_send)


def wants_html(request):
    return (
        request.method in {"GET", "HEAD"}
        and "text/html" in request.headers.get("accept", "")
        and not request.url.path.startswith(("/api", "/static/", "/docs", "/redoc", "/openapi"))
    )


class PageCompression(GZipMiddleware):
    async def __call__(self, scope, receive, send):
        # Geen hercompressie van beelden/video of gereflecteerde formulierinvoer.
        if (scope["type"] != "http" or scope["method"] != "GET"
                or scope["path"].startswith("/static/")
                or scope["path"] in {"/contact", "/offerte"}):
            return await self.app(scope, receive, send)
        await super().__call__(scope, receive, send)


def create_app():
    production = environment() == "production"
    application = FastAPI(debug=False, docs_url=None, redoc_url=None, openapi_url=None)
    application.add_middleware(PageCompression, minimum_size=1024, compresslevel=5)
    application.add_middleware(ResponsePolicy, production=production)

    @application.exception_handler(HTTPException)
    async def http_error(request: Request, exc: HTTPException):
        if exc.status_code == 404 and wants_html(request):
            return templates.TemplateResponse(
                request=request, name="404.html", context={}, status_code=404,
            )
        return JSONResponse({"detail": exc.detail}, status_code=exc.status_code, headers=exc.headers)

    @application.exception_handler(Exception)
    async def server_error(request: Request, exc: Exception):
        # Geen exceptiondetails of ingevulde gegevens in het antwoord.
        headers = {
            "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff",
            "Referrer-Policy": "strict-origin-when-cross-origin", "X-Frame-Options": "SAMEORIGIN",
            "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
        }
        if not production:
            headers["X-Robots-Tag"] = "noindex, nofollow"
        if wants_html(request):
            return templates.TemplateResponse(
                request=request, name="500.html", context={}, status_code=500,
                headers=headers,
            )
        return JSONResponse({"detail": "Internal Server Error"}, status_code=500,
                            headers=headers)

    @application.get("/robots.txt", include_in_schema=False)
    def robots():
        if not production:
            return PlainTextResponse("User-agent: *\nDisallow: /\n")
        return PlainTextResponse(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    @application.get("/sitemap.xml", include_in_schema=False)
    def sitemap():
        urls = "".join(f"  <url><loc>{SITE_URL}{path}</loc></url>\n" for path in PUBLIC_PAGES)
        return Response('<?xml version="1.0" encoding="UTF-8"?>\n'
                        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                        + urls + '</urlset>\n', media_type="application/xml")

    application.mount("/static", StaticFiles(directory="static"), name="static")
    application.include_router(paginas_router)
    return application


templates.context_processors.append(social_context)
app = create_app()
