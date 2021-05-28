# external
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# molar
from molar import __version__

from .api.api_v1.api import api_router
from .core.config import settings

app = FastAPI(
    title="Molar 🦷",
    version=__version__,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
