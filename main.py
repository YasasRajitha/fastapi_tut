from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message" : "Hello World"}

@app.post("/")
async def post():
    return{"message" : "Hello World from POST"}

@app.get("/items")
async def list_items():
    return{"message" : "List item routes"}

@app.get("/items/{item_id}")
async def get_item(item_id):
    return{"item_id" : item_id}