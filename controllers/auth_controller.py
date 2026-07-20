from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models.user import (
    UserRegister,
    UserLogin,
    ForgotPassword,
    ResetPassword,
)
from services import auth_service

router = APIRouter(tags=["Authentication"])

@router.post("/register")
def register(
    user: UserRegister,
    session: Session = Depends(get_session),
):
    return auth_service.register_user(session, user)

@router.post("/login")
def login(
    user: UserLogin,
    session: Session = Depends(get_session),
):
    return auth_service.login_user(session, user)

@router.post("/admin/register")
def admin_register(
    user: UserRegister,
    session: Session = Depends(get_session),
):
    return auth_service.register_admin(session, user)

@router.post("/admin/login")
def admin_login(
    user: UserLogin,
    session: Session = Depends(get_session),
):
    return auth_service.login_admin(session, user)

@router.post("/forget-password")
def forgot_password(
    request: ForgotPassword,
    session: Session = Depends(get_session),
):
    return auth_service.forgot_password(session, request)

@router.post("/reset-password")
def reset_password(
    request: ResetPassword,
    session: Session = Depends(get_session),
):
    return auth_service.reset_password(session, request)