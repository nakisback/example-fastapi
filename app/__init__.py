from fastapi import FastAPI
from .config import Settings
from contextlib import asynccontextmanager
from .config import settings
from .database import init_db




# lifespan code

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()

    yield

def create_app():
    app = FastAPI(
        description="This is a simple REST API for a book review service",
        title="Bookly",
        version=settings.VERSION,
        lifespan=lifespan
    )

    return app


app = create_app()