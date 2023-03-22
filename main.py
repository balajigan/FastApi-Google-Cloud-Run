from fastapi import FastAPI
from fastapi import Response
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
        
@app.get("/")
def home():
    return {"message": "Home Page"}

@app.get("/products")
def products():
    return {"Name": "product1"}

@app.get("/customers")
def products():
    return {"First Name": "John",
             "Last Name": "Smith",
             "Address": "1234 West RD"}

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Cheese", price=12.0),
        Item(name="Catchup", price=19.0),
    ]

