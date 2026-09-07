from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.paginas import router as paginas_router


app = FastAPI()


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)


app.include_router(paginas_router)