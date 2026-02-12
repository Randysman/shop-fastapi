from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .config import settings
from .database import init_db
from .routes import prod_router, cat_router, cart_router


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url='/api/docs',
    redoc_url='/api/redoc'
)

app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins,
                   allow_credential=True, allow_methods=["*"],
                   allow_headers=["*"])

app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")


@app.get("/")
def root():
    return {"message": "Добро пожаловать!"}

