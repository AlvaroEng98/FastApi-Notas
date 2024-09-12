from fastapi import FastAPI 
from enum import Enum


app = FastAPI()

#una clase que herrede de enum para definir una lista de valores posibles
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name, "message":"Deep Learning FTW!"}
    if model_name.value == 'lenet':
        return {"model_name":model_name, "message":"LeCNN all the images"}
    
    return {"model_name":model_name, "message":"Have some residuals"}

#usando un convertidor de ruta
@app.get('/files/{path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}