from fastapi import HTTPException
from sqlmodel import Session, select

from models.user import (
    User,
    UserRegister,
    UserLogin,
    ForgotPassword,
    ResetPassword,
)

from auth import (
    authenticate_user,
    create_access_token,
    hash_password,
)

def register_user(session: Session, user: UserRegister):

    existing_user = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    db_user = User(
        fullname=user.fullname,
        email=user.email,
        password=hash_password(user.password),
        role="user",
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return {
        "message": "User registered successfully",
        "user_id": db_user.id,
    }


# -------------------------
# ADMIN REGISTER
# -------------------------
def register_admin(session: Session, user: UserRegister):

    existing_user = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    db_admin = User(
        fullname=user.fullname,
        email=user.email,
        password=hash_password(user.password),
        role="admin",
    )

    session.add(db_admin)
    session.commit()
    session.refresh(db_admin)

    return {
        "message": "Admin registered successfully",
        "admin_id": db_admin.id,
    }


# -------------------------
# USER LOGIN
# -------------------------
def login_user(session: Session, user: UserLogin):

    db_user = authenticate_user(
        session,
        user.email,
        user.password,
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


# -------------------------
# ADMIN LOGIN
# -------------------------
def login_admin(session: Session, user: UserLogin):

    db_user = authenticate_user(
        session,
        user.email,
        user.password,
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if db_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Access denied. Admins only.",
        )

    access_token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


# -------------------------
# FORGOT PASSWORD
# -------------------------
def forgot_password(session: Session, data: ForgotPassword):

    user = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "message": "Password reset request received",
    }


# -------------------------
# RESET PASSWORD
# -------------------------
def reset_password(session: Session, data: ResetPassword):

    user = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    user.password = hash_password(data.new_password)

    session.add(user)
    session.commit()

    return {
        "message": "Password reset successful",
    }