# CRUD Products API with FastAPI

A RESTful API built with **FastAPI**, **SQLModel**, and **PostgreSQL** that performs Create, Read, Update, and Delete (CRUD) operations on products.

## Features

* Create a new product
* Retrieve all products with pagination
* Retrieve a product by ID
* Update a product
* Delete a product
* PostgreSQL database integration
* Interactive API documentation with Swagger UI

## Technologies Used

* Python 3
* FastAPI
* SQLModel
* PostgreSQL
* SQLAlchemy
* Psycopg2
* Python Dotenv
* fastapi dev

## Project Structure

```text
crud-products-fastapi/
│
├── controllers/
│   |─ product_controller.py
│
├── models/
│   |── product.py
│
├── services/
│   |── product_service.py
│
├── database.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## Installation

### Clone the repository

```bash
git clone https://github.com/kennewest12/crud-products-fastapi.git
```

### Navigate into the project

```bash
cd crud-products-fastapi
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Configure the Database

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql+psycopg2://your_username:your_password@localhost:5432/crud_products
```

Replace:

* `your_username`
* `your_password`
* `crud_products`

with your PostgreSQL credentials.

## Run the Application

Using FastAPI CLI:

```bash
fastapi dev
```

Or using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| GET    | `/products`              | Get all products     |
| GET    | `/products/{product_id}` | Get a product by ID  |
| POST   | `/products`              | Create a new product |
| PUT    | `/products/{product_id}` | Update a product     |
| DELETE | `/products/{product_id}` | Delete a product     |

## Sample Request

```json
{
  "name": "Laptop",
  "description": "Dell Inspiron 15",
  "cost": 850.50,
  "picture": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ]
}
```

## Author

**Kenneth**

* GitHub: https://github.com/kennewest12
* Role: IT Support Engineer | 