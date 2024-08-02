# FastAPI

## Setup Python Path

Make sure python is accessible from the command line:

[projectRoot]
``` shell
python --version
```

If Python is not accessible from the command line, then add the path to the parent folder of python.exe to your environment variables system path (Windows):

Example python path:
``` shell
C:\Users\{YOUR_USERNAME}\AppData\Local\Programs\Python\Python310
```

Note, the path must be difined in your `Path` variable under `system`, not `user` environment variables.

## Note

You may have to run `python` CLI commands outside of `vscode`'s terminal. You can try using a `powershell` terminal outside of `vscode` if you are not seeing `vscode`'s terminal successfully recognizing the `python` command. 

## Using pip on Windows

``` shell
python -m pip install [packagename]
```

Check to see that pip is working:
``` shell
python -m pip --version
```

## Youtube Tutorial

[Python FastAPI Tutorial: Build a REST API in 15 Minutes
](https://www.youtube.com/watch?v=iWS9ogMPOI0)

The following tutorial is based on the above YouTube tutorial with some additional notes about using `.bat` scripts to save and make API requests more conveniently. 

## Install fastapi

[projectRoot]
``` shell
python -m pip install fastapi
```

## Install uvicorn

[projectRoot]
``` shell
python -m pip install uvicorn
```

`uvicorn` is the server used to test and run `fastapi` applications.

## Create a Hi World Server and Endpoint

Create a `main.py` file:

[projectRoot]/src/main.py
``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hi": "World"}
```

Run the server:

[projectRoot]/src:
``` shell
cd ./src
uvicorn main:app --reload
```

Note: Remember to run this command in a separate `powershell` terminal outside of `vscode` or the command may not be recognized within `vscode`.

The server should run at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) by default. You should see your `{"Hi": "World"}` message when accessing this url.

Normally, GET requests can be made directly through the browser, but for the sake of convenience, a curl command in the terminal can also be used to make a GET request:

``` shell
curl http://127.0.0.1:8000/
# Output: {"Hi":"World!"}
```

Note: for convenience, I have wrapped this sample `curl` request in a `.bat` script. Just run the following to execute this `curl` GET command:

[projectRoot]/
``` shell
.\bat\get.bat
# Output: {"Hi":"World!"}
```

`--reload` flag causes the server to automatically refresh every time changes are made to `main.py`. When you make changes, you will see the server logs indicate the server restarted. You will still need to refresh the browser page to see the changes.

## Post Endpoint

Add the following to `main.py`:

``` python
items = []

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items
```

`item: str` is a parameter coming from the post request.

`item` will be appended to the array, `items`, then the `items` array will be returned to the frontend.

To post a new item to the `items` endpoint, the following terminal `curl` command can be used:

``` shell
# request 1
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/items?item=grap
# Output: ["grape"]

# request 2
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/items?item=pear
# Output: ["grape","pear"]
```

Note: for convenience, I have wrapped this sample post command in a `.bat` script. Just run the following to execute this `curl` POST command:

[projectRoot]/
``` shell
.\bat\post.bat {fruitName}

.\bat\post.bat grape
# Output: ["grape"]

.\bat\post.bat pear
# Output: ["grape","pear"]
```

## Getting an Item By its Index

Added a new route to `main.py`:

``` python
@app.get("/item")
def get_item(item_index: int):
    return items[item_index]
```

Make sure `items` contains two items:

``` shell
.\bat\post.bat cherry
# Output: ["cherry"]

.\bat\post.bat banana
# Output: ["cherry", "banana"]
```

Use the new endpoint to get one of the items by its index:

``` shell
curl http://127.0.0.1:8000/item?item_index=0
# Output: "cherry"
```

Or use the convenience `.bat` file:

``` shell
.\bat\get_by_index.bat 0
# Output: "cherry"

.\bat\get_by_index.bat 1
# Output: "banana"

.\bat\get_by_index.bat 2
# Output: Internal Server Error
```

Notice, since the last request provided an index out of range, an `Internal Server Error` was triggered. 

