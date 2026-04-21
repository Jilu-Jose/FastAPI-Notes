from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Hello Earthlings"}


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/predict/")
def ml_predict(value: float, value2: float):
    res = (value ** 2) + (value2 ** 3) + 0.98
    return {"prediction": res}


@app.post("/item/")
def create_item(item:Item):
    return {"item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated": item}


@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}


