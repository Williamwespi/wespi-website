from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.proxy_headers import ProxyHeadersMiddleware

from routes.paginas import router as paginas_router


app = FastAPI()


# Railway gebruikt een proxy voor HTTPS.
# Hierdoor weet FastAPI dat de oorspronkelijke
# bezoeker de website via HTTPS opent.
app.add_middleware(
    ProxyHeadersMiddleware,
    trusted_hosts="*",
)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)


app.include_router(paginas_router)