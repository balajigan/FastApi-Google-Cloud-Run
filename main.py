from fastapi import FastAPI
from fastapi import Response

app = FastAPI()

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
