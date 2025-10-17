# app/schemas/auth.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: EmailStr
    exp: Optional[int] = None  


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class RefreshOut(Token):
    expires_at: Optional[datetime] = None

