from enum import Enum
from typing import Annotated
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

from fastapi import Depends, FastAPI

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None 


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI() 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/security")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals "}

@app.post("/itemszzzz")
async def create_item(item: Item):
    return item 


@app.post("/getit")
async def postSomething():
    return {"random":"cow is life "}

@app.get("/items/{items_id}")
async def read_item(item_id: int):
    return {"item_id":item_id}
