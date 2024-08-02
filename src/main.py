from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"Hi": "World!"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/item/{item_index}")
def get_item(item_index: int):
    if item_index < len(items):
        return items[item_index]
    else:
        raise HTTPException(status_code=404, detail=f"404 Not found: Index({item_index}) out of range in Length({len(items)})")