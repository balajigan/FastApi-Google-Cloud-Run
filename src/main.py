# main py file
#from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi import Response
from fastapi import Request
from pydantic import BaseModel
from fastapi.responses import FileResponse
from cloudrun import CloudRun
from pubsub import PubSub

import os
from google.cloud import pubsub_v1

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = ['Project ID1', 'Project ID2', 'Project ID3', 'Project ID4', 'Project ID5']

class LookupData(BaseModel):
    project_id: list[str] = ['Project_ID1', 'Project_ID2', 'Project_ID3', 'Project_ID4', 'Project_ID4']
    region_name: list[str] = ['us-east1', 'us-east2', 'us-east3', 'us-east4']    
    zone_name: list[str] = ['us-east1-a', 'us-east2-b', 'us-east2-c']
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
#    pubSub = PubSub()
#    pubSub.registerSubscriber()
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

@app.post("/gcp-resources/cloud-run")
def createCloudRun(cloudRun : CloudRun):
#    reqested_resource = cloudRun.json()
    pubSub = PubSub()
    pubSub.publishMessage(cloudRun.resource_type,cloudRun.json())
    print(cloudRun)
    return {
        "status" : "SUCCESS",
        "data" : cloudRun.json()
    }

#@app.post("/files/")
#async def create_file(file: Annotated[bytes, File()]):
#    return {"file_size": len(file)}

@app.get("/download-file")
def download_file():
    file_path = "main.py"
    directory = os.system('pwd')
    print(directory)
    return FileResponse(path=file_path, filename=file_path)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

def callback(message):
    print('The subscriber callback method is called')
    print(message.data)
    message.ack()
    
topic_name = 'projects/mytemporaryproject28490/topics/gcp-resource-topic'
subscription_name = 'projects/mytemporaryproject28490/subscriptions/gcp-resource-topic-sub'
with pubsub_v1.SubscriberClient() as subscriber:
    future = subscriber.subscribe(subscription_name, callback)
    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()
