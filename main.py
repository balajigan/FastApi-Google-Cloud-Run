from fastapi import FastAPI
from fastapi import Response
from fastapi import Request
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = ['Project ID1', 'Project ID2', 'Project ID3']

class LookupData(BaseModel):
    project_id: list[str] = ['Project ID1', 'Project ID2', 'Project ID3']
    region_name: list[str] = ['us-east1', 'us-east2']    
    zone_name: list[str] = ['us-east1-a', 'us-east2-b']
    network : list[str] = ['network1', 'network2']   
    subnetwork : list[str] = ['subnetwork1', 'subnetwork2']                          
        
class Customer(BaseModel):
    FirstName: str
    LastName: str    
    Address: str
    State: str
    Phone: str
          
@app.get("/")
def Help():
    return [LookupData()]

                              
                              
@app.get("/products")
def products():
    return {"Name": "product1"}

@app.get("/customers")
def customers():
    return [
        Customer(FirstName="John", LastName="Walter", Address="123 willson Rd, Apt 456", State="TX", Phone="123-456-7890"),
        Customer(FirstName="Raj", LastName="Kumar", Address="1367 Bend Rd, Apt 456", State="MN", Phone="230-564-8790"),
        Customer(FirstName="Victor", LastName="Frank", Address="2783 Nelson Rd, Apt 456", State="CA", Phone="312-645-0890"),
    ]

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Cheese", price=12.0),
        Item(name="Catchup", price=19.0),
    ]

@app.post("/gcp-resources")
def gcpResources(item : Item):
#    reqested_resource = resource.json()
    return {
        "status" : "SUCCESS"
#        "data" : item
    }
