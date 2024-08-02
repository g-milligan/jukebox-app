from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"Hi": "World!"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/item")
def get_item(item_index: int):
    return items[item_index]