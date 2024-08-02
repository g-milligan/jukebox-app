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

`--reload` flag causes the server to automatically refresh every time changes are made to `main.py`. When you make changes, you will see the server logs indicate the server restarted. You will still need to refresh the browser page to see the changes.


