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
                 
@app.get("/")
def Help():
#    pubSub = PubSub()
#    pubSub.registerSubscriber()
    return [LookupData()]
                                                      
@app.post("/gcp-resources/cloud-run")
def createCloudRun(cloudRun : CloudRun):
#    reqested_resource = cloudRun.json()
    print('project Id = ')
    print('$PROJECT_ID')
    print(os.environ['PROJECT_ID'])
    
    pubSub = PubSub()
    pubSub.publishMessage(cloudRun.resource_type,cloudRun.json())
    print(cloudRun)
    return {
        "status" : "SUCCESS",
        "data" : cloudRun.json()
    }

@app.get("/download-file")
def download_file():
    file_path = "main.py"
    directory = os.system('pwd')
    print(directory)
    return FileResponse(path=file_path, filename=file_path)


#@app.post("/uploadfile/")
#async def create_upload_file(file: UploadFile):
#    return {"filename": file.filename}

def callback(message):
    print('The subscriber callback method is called')
    print(message.data)
    message.ack()
    
topic_name = 'projects/mytemporaryproject28490/topics/gcp-resource-topic'
subscription_name = 'projects/mytemporaryproject28490/subscriptions/gcp-resource-topic-sub'
with pubsub_v1.SubscriberClient() as subscriber:
    future = subscriber.subscribe(subscription_name, callback)
#    try:
#        future.result()
#    except KeyboardInterrupt:
#        future.result()
        #future.cancel()
