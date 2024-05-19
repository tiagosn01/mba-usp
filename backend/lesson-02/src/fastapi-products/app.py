from fastapi import FastAPI
from models.product import Product

app = FastAPI()

@app.get('/')
def hello_world():
    """First endpoint Hello World"""
    return {
        "response": "Hello World"
    }


@app.get('/api/ola/{name}')
def hello(name: str):
    """Endpoint for return name"""
    
    if not name:
        pass
    return {
        "Olá": name
    }

data = [
    Product(id=1, name='Tenis Nike Air', description='Calçado muito legal', price=249.99),
    Product(id=2, name='Iphone', description='Celulares', price=249.99),
    Product(id=3, name='Samsung', description='Celulares', price=249.99),
]

@app.get('/api/products')
def get_products(): 
    """List all products"""
    return data


@app.get('/api/products/{id}')
def get_product_by_id(id: int):
    """Get Product by id"""
    for product in data:
        if product.id == id:
            return product
    return {"message": "Product not found!"}