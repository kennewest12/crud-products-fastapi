from typing import Optional
from datetime import datetime
from enum import Enum
from sqlmodel import SQLModel, Field


class OrderStatus(str, Enum):
    pending = "Pending"
    processing = "Processing"
    shipped = "Shipped"
    delivered = "Delivered"
    cancelled = "Cancelled"


class OrderItemCreate(SQLModel):
    product_id: int
    quantity: int = 1


class OrderCreate(SQLModel):
    items: list[OrderItemCreate]


class OrderStatusUpdate(SQLModel):
    status: OrderStatus


class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    order_id: int = Field(foreign_key="order.id")
    product_id: int = Field(foreign_key="product.id")

    quantity: int = 1


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")

    status: OrderStatus = Field(default=OrderStatus.pending)

    total_cost: float = 0

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)