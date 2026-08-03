from datetime import datetime
from fastapi import HTTPException
from sqlmodel import Session
from models.order import (
    Order,
    OrderItem,
    OrderCreate,
    OrderStatusUpdate,
)
from models.product import Product
from models.user import User
from services.email_service import send_email

def create_order(
    session: Session,
    order: OrderCreate,
    current_user: User,
):

    total_cost = 0

    db_order = Order(
        user_id=current_user.id,
        total_cost=0,
    )

    session.add(db_order)
    session.commit()
    session.refresh(db_order)

    for item in order.items:

        product = session.get(Product, item.product_id)

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found",
            )

        total_cost += product.cost * item.quantity

        order_item = OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
        )

        session.add(order_item)

    db_order.total_cost = total_cost
    db_order.updated_at = datetime.utcnow()

    session.add(db_order)
    session.commit()
    session.refresh(db_order)

    # Build order summary
    order_summary = ""

    for item in order.items:
        product = session.get(Product, item.product_id)

        order_summary += (
            f"{product.name} x {item.quantity} "
            f"= ${product.cost * item.quantity}\n"
        )

    body = f"""
    Hello {current_user.fullname},

    Your order has been placed successfully.

    Order ID: {db_order.id}

    Order Summary:
    {order_summary}

    Total Cost: ${db_order.total_cost}

    Status: {db_order.status}

    Thank you for shopping with us.
    """

    send_email(
        to_email=current_user.email,
        subject="Order Confirmation",
        body=body,
    )

    return db_order


def update_order_status(
    session: Session,
    order_id: int,
    order_status: OrderStatusUpdate,
):

    db_order = session.get(Order, order_id)

    if not db_order:
        return None

    # Update the order status
    db_order.status = order_status.status
    db_order.updated_at = datetime.utcnow()

    session.add(db_order)
    session.commit()
    session.refresh(db_order)

    # Get the user who owns the order
    user = session.get(User, db_order.user_id)

    body = f"""
Hello {user.fullname},

Your order status has been updated.

Order ID: {db_order.id}

New Status: {db_order.status}

Thank you for shopping with us.
"""

    send_email(
        to_email=user.email,
        subject="Order Status Updated",
        body=body,
    )

    return db_order