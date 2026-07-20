from typing import Optional
from sqlmodel import SQLModel, Field

class UserRegister(SQLModel):
    fullname: str
    email: str
    password: str

class UserLogin(SQLModel):
    email: str
    password: str

class ForgotPassword(SQLModel):
    email: str

class ResetPassword(SQLModel):
    email: str
    new_password: str

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    fullname: str
    email: str = Field(index=True, unique=True)

    password: str

    role: str = "user"