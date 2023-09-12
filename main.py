from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/getit")
async def postSomething():
    return {"random":"cow is life "}

@app.get("/items/{items_id}")
async def read_item(item_id: int):
    return {"item_id":item_id}
