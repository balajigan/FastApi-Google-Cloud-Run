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
    return {\n"First Name": "John", \n
             "Last Name": "Smith", \n
             "Address": "1234 West RD" \n}
