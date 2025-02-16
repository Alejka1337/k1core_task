from datetime import datetime, timedelta, timezone

from django.conf import settings
from jose import jwt


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token=token,
        key=settings.SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM]
    )


def create_access_token(token_payload: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXPIRATION_MINUTES)
    token_payload.update({"exp": expire})

    access_token = jwt.encode(
        claims=token_payload,
        key=settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM)

    return access_token
