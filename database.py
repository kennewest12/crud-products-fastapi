import os
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
from models.product import Product
from models.user import User

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url, echo=True)


def create_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session