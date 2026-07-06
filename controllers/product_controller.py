#controllers/product_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
import services.product_service as product_service
from models.product import ProductCreate, ProductUpdate

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
    session: Session = Depends(get_session)
):
    return product_service.create_product(session, product)


@router.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
    session: Session = Depends(get_session)
):
    updated = product_service.update_product(session, product_id, product)

    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    deleted = product_service.delete_product(session, product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted successfully"}