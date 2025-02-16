"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# django setup
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django_app = get_asgi_application()


# fastapi setup
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers import auth_router, blocks_router

fastapi_app = FastAPI()
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


fastapi_app.mount("/django", django_app)

os.makedirs('static', exist_ok=True)
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")

fastapi_app.include_router(auth_router)
fastapi_app.include_router(blocks_router)


@fastapi_app.get("/")
async def root():
    return {"message": "FastAPI + Django integration successful!"}
