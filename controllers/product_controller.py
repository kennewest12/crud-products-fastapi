#controllers/product_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
import services.product_service as product_service
from models.product import ProductCreate, ProductUpdate
from auth import get_current_admin
from models.user import User

router = APIRouter()


@router.get("/products")
def get_products(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session)
):
    return product_service.get_products(session, skip, limit)


@router.get("/products/{product_id}")
def get_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    product = product_service.get_product(session, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products")
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin)
):
    return product_service.create_product(
        session,
        product,
        current_admin,
    )

@router.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
):

    updated = product_service.update_product(
        session,
        product_id,
        product,
        current_admin,
    )

    if updated is None:
        raise HTTPException(status_code=404, detail="Product not found")

    if updated == "unauthorized":
        raise HTTPException(
            status_code=403,
            detail="You can only update your own products",
        )

    return updated

@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    session: Session = Depends(get_session),
    current_admin: User = Depends(get_current_admin),
):

    deleted = product_service.delete_product(
        session,
        product_id,
        current_admin,
    )

    if deleted is None:
        raise HTTPException(status_code=404, detail="Product not found")

    if deleted == "unauthorized":
        raise HTTPException(
            status_code=403,
            detail="You can only delete your own products",
        )

    return {"message": "Product deleted successfully"}