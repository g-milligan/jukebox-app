# FastAPI (part 2)

## Introduction

If you have not already read [FastAPI (part 1)](./01_FastAPI.md) please go back and follow this previous part first.

This next tutorial will modify the `main.py` script from part one with additional features and enhancements. 

Whenever `main.py` is mentioned, this refers to `src2/main.py` instead of `src1/main.py` from the previous tutorial.

## Convenience scripts for this part 2

Some of the convenience scripts have been updated for part 2 of this tutorial. 

Here are all of the convenience script commands that can be used in part 2:
``` shell

# get hi world message
.\learn\fastapi\bat\get.bat 

# get items saved in memory
.\learn\fastapi\bat\get_all {optional:limit}

# get one of the items saved in memory
.\learn\fastapi\bat\get_by_index.bat {index}

# load multiple items into memory
.\learn\fastapi\bat\load_multiple_items2.bat

# load one item into memory
.\learn\fastapi\bat\post2.bat {item} {optional:is_done}
```

## pydantic Classes used for data Models

You can enforce specific data structures in the python FastAPI. 

For example, each item stored can have both a `text` and `is_done` field.

Add this to the `main.py` file:

``` python
from pydantic import BaseModel

class Item(BaseModel):
    text: str # required because a default value is not given
    is_done: bool = False # not required because a default value is given
```

Now this "model" item data structure can be used in requests instead of just accepting a `str` type for items:

``` python

# updated the array item type to be "Item"
@app.post("/items")
def create_item(item: list[Item]):
    items.extend(item) # extend will spread multiple items into the array
    return items

# updated the return type to be "Item"
@app.get("/item/{item_index}")
def get_item(item_index: int) -> Item:
    if item_index < len(items):
        return items[item_index]
    else:
        raise HTTPException(status_code=404, detail=f"404 Not found: Index({item_index}) out of range in Length({len(items)})")
```

## Response Models

Similar to using `pydantic` to define request models (example above), response models can also be defined.

`main.py` changes:

For any request, add the second `response_model` parameter to specifiy the expected response return type. For example:

``` python
...
@app.post("/items", response_model=list[Item])
...
@app.get("/items", response_model=list[Item])
...
@app.get("/item/{item_index}", response_model=Item)
...
```

## Interactive Documentation

In order to run the server endpoints, `curl` commands and convenience scripts have been used through the terminal.

FastAPI provides another way of interacting with the API. You can access an automatically generated `swagger` page through the server path `/docs`.

[Swagger Documentation: http://localhost:8000/docs](http://localhost:8000/docs)

Another documentation format that may be easer to read is `redoc`:

[Redoc: http://localhost:8000/redoc](http://localhost:8000/redoc)

Convenience scripts may still be faster, but swagger docs provide an additional way to view and test APIs.

<hr />

(end of FastAPI tutorial)

[Back to learning Home](../../README.md)