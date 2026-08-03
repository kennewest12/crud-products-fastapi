from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from auth import get_current_user, get_current_admin
from models.user import User
from models.order import OrderCreate, OrderStatusUpdate
import services.order_service as order_service

router = APIRouter(tags=["Orders"])


@router.post("/order")
def create_order(
    order: OrderCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return order_service.create_order(
        session,
        order,
        current_user,
    )


@router.put("/order/{order_id}/status")
def update_order_status(
    order_id: int,
    order_status: OrderStatusUpdate,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
):

    order = order_service.update_order_status(
        session,
        order_id,
        order_status,
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order