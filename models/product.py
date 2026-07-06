from typing import List, Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY


class ProductCreate(SQLModel):

    name: str
    description: str
    cost: float
    picture: List[str]


class ProductUpdate(SQLModel):

    name: Optional[str] = None
    description: Optional[str] = None
    cost: Optional[float] = None
    picture: Optional[List[str]] = None


class Product(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    cost: float
    picture: List[str] = Field(
        sa_column=Column(ARRAY(String))
    )

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)