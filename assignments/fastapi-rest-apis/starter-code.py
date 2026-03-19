from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: str


items = [
    Item(id=1, name="Notebook", description="A notebook for class notes"),
    Item(id=2, name="Backpack", description="A backpack for school supplies"),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API"}


@app.get("/items")
def get_items():
    return {"items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    for existing_item in items:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")

    items.append(item)
    return {"message": "Item created successfully", "item": item}