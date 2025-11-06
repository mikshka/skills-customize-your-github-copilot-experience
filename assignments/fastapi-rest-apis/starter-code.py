"""Minimal FastAPI starter app for the assignment.

Run with:
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload --port 8000

This app uses an in-memory dict to store items.
"""
from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Simple Items API", version="0.1")


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


# In-memory storage
_items = {}
_id_counter = 0


@app.get("/", summary="API root")
def root():
    return {"message": "Welcome to the Simple Items API. See /docs for OpenAPI UI."}


@app.get("/items", summary="List items")
def list_items():
    return list(_items.values())


@app.get("/items/{item_id}", summary="Get item by id")
def get_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@app.post("/items", status_code=status.HTTP_201_CREATED, summary="Create item")
def create_item(item: Item):
    global _id_counter
    _id_counter += 1
    obj = item.dict()
    obj["id"] = _id_counter
    _items[_id_counter] = obj
    return obj


@app.put("/items/{item_id}", summary="Update item")
def update_item(item_id: int, item: Item):
    if item_id not in _items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    obj = item.dict()
    obj["id"] = item_id
    _items[item_id] = obj
    return obj


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete item")
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del _items[item_id]
    return None
