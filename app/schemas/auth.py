from pydantic import BaseModel


class SignUpRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class SighUpResponse(BaseModel):
    message: str = "User successfully created"
