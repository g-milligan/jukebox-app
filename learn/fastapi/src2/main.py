from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    text: str # required because a default value is not given
    is_done: bool = False # not required because a default value is given

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"Hi": "Part 2 FastAPI"}

@app.post("/items", response_model=list[Item])
def create_item(item: list[Item]) -> list[Item]:
    items.extend(item) # extend will spread multiple items into the array
    return items

@app.get("/items", response_model=list[Item])
def list_items(limit: int) -> list[Item]:
    # get items in the array from index range 0 to a given limit
    return items[0:limit]

@app.get("/item/{item_index}", response_model=Item)
def get_item(item_index: int) -> Item:
    if item_index < len(items):
        return items[item_index]
    else:
        raise HTTPException(status_code=404, detail=f"404 Not found: Index({item_index}) out of range in Length({len(items)})")