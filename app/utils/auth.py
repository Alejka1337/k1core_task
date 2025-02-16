from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from app.dal.auth import get_user_by_id
from app.exceptions import NotValidCredentialsException, UserNotFoundException
from app.models import User
from app.utils.jwt import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-in")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = decode_access_token(token)
    except JWTError:
        raise NotValidCredentialsException()

    user = get_user_by_id(payload["user_id"])
    if not user:
        raise UserNotFoundException()

    return user
