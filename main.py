from fastapi import FastAPI
from database import create_db
from controllers import product_controller

app = FastAPI(
    title="Products API"
)


@app.on_event("startup")
def startup():
    create_db()


app.include_router(product_controller.router)

