from datetime import datetime
from sqlmodel import Session, select
from models.product import Product, ProductCreate, ProductUpdate
from models.user import User


def create_product(session: Session, product: ProductCreate, current_admin: User):

    db_product = Product(**product.model_dump(), admin_id=current_admin.id)
    
    session.add(db_product)
    session.commit()
    session.refresh(db_product)

    return db_product


def get_products(session: Session, skip: int = 0, limit: int = 10):
    statement = select(Product).offset(skip).limit(limit)

    return session.exec(statement).all()


def get_product(session: Session, product_id: int):

    return session.get(Product, product_id)


def update_product(
    session: Session,
    product_id: int,
    product: ProductUpdate,
    current_admin: User,
):

    db_product = session.get(Product, product_id)

    if not db_product:
        return None

    if db_product.admin_id != current_admin.id:
        return "unauthorized"

    updates = product.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(db_product, key, value)

    db_product.updated_at = datetime.utcnow()

    session.add(db_product)
    session.commit()
    session.refresh(db_product)

    return db_product


def delete_product(
    session: Session,
    product_id: int,
    current_admin: User,
):

    db_product = session.get(Product, product_id)

    if not db_product:
        return None

    if db_product.admin_id != current_admin.id:
        return "unauthorized"

    session.delete(db_product)
    session.commit()

    return True