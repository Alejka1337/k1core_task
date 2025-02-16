from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.dal.auth import user_create, user_login
from app.schemas.auth import SighUpResponse, SignUpRequest, TokenResponse

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    path="/sign-up",
    status_code=status.HTTP_201_CREATED,
    response_model=SighUpResponse
)
def sigh_up(data: SignUpRequest):
    return user_create(data=data)


@auth_router.post(
    path="/sign-in",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse
)
def sign_in(form_data: OAuth2PasswordRequestForm = Depends()):
    return user_login(form_data=form_data)
