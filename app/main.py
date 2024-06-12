from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import events
from app.config import settings

app = FastAPI(title=settings.API_NAME, version=settings.VERSION)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(events.router, prefix="/events", tags=["Events"])