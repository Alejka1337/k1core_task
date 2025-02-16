from django.contrib.auth import authenticate, get_user_model
from fastapi.security import OAuth2PasswordRequestForm

from app.exceptions import NotValidCredentialsException, UserDoesExistsExException
from app.schemas import SighUpResponse, SignUpRequest, TokenResponse
from app.utils.jwt import create_access_token

User = get_user_model()


def get_user_by_id(user_id: int):
    return User.objects.filter(id=user_id).first()


def user_create(data: SignUpRequest) -> SighUpResponse:
    if User.objects.filter(username=data.username).exists():
        raise UserDoesExistsExException()

    user = User(username=data.username)
    user.set_password(data.password)
    user.save()

    return SighUpResponse()


def user_login(form_data: OAuth2PasswordRequestForm) -> TokenResponse:
    credentials = {"username": form_data.username, "password": form_data.password}
    user = authenticate(**credentials)
    if user is None:
        NotValidCredentialsException()

    token_payload = {
        "user_id": user.id,
        "username": user.username,
    }

    access_token = create_access_token(token_payload=token_payload)
    return TokenResponse(access_token=access_token)
