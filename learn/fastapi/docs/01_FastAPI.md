# FastAPI (part 1)

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

If setting the environment variable in the path still fails, you can define `python` as an alias for your powershell sessions:

``` shell
# create or open an existing profile for powershell
 notepad $PROFILE

# This should open a text file. Paste your alias into the profile text file (adjust the path to match your local python.exe path):
Set-Alias python "C:\Users\{USER}\AppData\Local\Programs\Python\Python310\python.exe"
```

This alias should continue to persist between powershell sessions. 

Note: A powershell profile is a set of instructions to run, when you first begin a powershell session. 

In this documentation, any command starting with `python` will be run through the powershell terminal since powershell is configured to recognize "python" as an alias.

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

From here to the end of this FastAPI tutorial, I am following the steps from this excellent YouTube tutorial:

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

[projectRoot]/learn/fastapi/src1/main.py
``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hi": "World"}
```

Run the server:

[projectRoot]/learn/fastapi/src1:
``` shell
cd ./learn/fastapi/src1
python -m uvicorn main:app --reload
```

Note: Remember to run this command in a separate `powershell` terminal outside of `vscode` or the command may not be recognized within `vscode`.

Note: A convenience powershell script was made to run the fastAPI server:

``` shell
# run the main.py server through a convenience script (shorter command)
./run.ps1
```

The server should run at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) by default. You should see your `{"Hi": "World"}` message when accessing this url.

Normally, GET requests can be made directly through the browser, but for the sake of convenience, a curl command in the terminal can also be used to make a GET request:

``` shell
curl http://127.0.0.1:8000/
# Output: {"Hi":"World!"}
```

Note: for convenience, I have wrapped this sample `curl` request in a `.bat` script. Just run the following to execute this `curl` GET command:

[projectRoot]/
``` shell
.\learn\fastapi\bat\get.bat
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
.\learn\fastapi\bat\post.bat {fruitName}

.\learn\fastapi\bat\post.bat grape
# Output: ["grape"]

.\learn\fastapi\bat\post.bat pear
# Output: ["grape","pear"]
```

## Getting an Item By its Index

Added a new route to `main.py`:

``` python
@app.get("/item/{item_index}")
def get_item(item_index: int):
    return items[item_index]
```

Make sure `items` contains two items:

``` shell
.\learn\fastapi\bat\post.bat cherry
# Output: ["cherry"]

.\learn\fastapi\bat\post.bat banana
# Output: ["cherry", "banana"]
```

Use the new endpoint to get one of the items by its index:

``` shell
curl http://127.0.0.1:8000/item/0
# Output: "cherry"
```

Or use the convenience `.bat` file:

``` shell
.\learn\fastapi\bat\get_by_index.bat 0
# Output: "cherry"

.\learn\fastapi\bat\get_by_index.bat 1
# Output: "banana"

.\learn\fastapi\bat\get_by_index.bat 2
# Output: Internal Server Error
```

Notice, since the last request provided an index out of range, an `Internal Server Error` was triggered. 

## Error Handling

Instead of throwin a `Internal Server Error` a better error would be [404 not found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404). 

Note: [Visit MDN to see more error documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

Update the `main.py` route:

``` python
@app.get("/item/{item_index}")
def get_item(item_index: int):
    if item_index < len(items):
        return items[item_index]
    else:
        raise HTTPException(status_code=404, detail=f"404 Not found: Index({item_index}) out of range in Length({len(items)})")
```

If the given index is out of range, a better error message with exception status `404` will be returned.

``` shell
.\learn\fastapi\bat\get_by_index.bat 2
# Output: {"detail":"404 Not found: Index(2) out of range in Length(0)"}
```

In order to throw this type of exception, the import statement in `main.py` was also updated to include `HTTPException`:

``` python
from fastapi import FastAPI, HTTPException
```

## Get all Items

New route code to add to `main.py`:
``` python
@app.get("/items")
def list_items(limit: int):
    # get items in the array from index range 0 to a given limit
    return items[0:limit]
```

Quickly create many items in the database with a convenience `.bat` script:

``` shell
.\learn\fastapi\bat\load_multiple_items.bat
```

Call the endpoint with a limit of 5:

``` shell
curl http://127.0.0.1:8000/items?limit=5
# Sample Output: ["blueberry","grape","watermellon","peach","orange"]
```

Convenience script, called with a limit of 5:

``` shell
.\learn\fastapi\bat\get_all.bat 5
# Sample Output: ["blueberry","grape","watermellon","peach","orange"]
```

## Next (part 2)
[Go to "FastAPI (part 2) &gt;&gt;"](./02_FastAPI.md)