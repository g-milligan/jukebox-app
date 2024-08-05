# PostgreSQL (part 2)

## Summary of Available Database Scripts

In the previous tutorial, we created a database, defined its schema, and loaded the database with starter data through an `.sql` script, by running two different `powershell` scripts:

`[projectRoot]/learn/postgresql_crud/powershell/`:
``` shell
# create the database "mydb_example" and define its schema
./create-schema.ps1

# insert sample starter data into the database
./load-data.ps1
```

For convenience, additional `powershell` scripts are available:

`[projectRoot]/learn/postgresql_crud/powershell/`:
``` shell
# login to the PostgreSQL command line terminal
./psql_login.ps1

# delete the database "mydb_example" to reset and start over
./drop-database-reset.ps1
```
## FastAPI first endpoint

The first endpoint will be simple, just meant to prove it is working by responding with `{message: "Hi, World!"}`.

`[projectRoot]learn\postgresql_crud\src\main.py`
``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hi, World!"}
```

Note: Since it was already covered in the `FastAPI` tutorial, installing `FastAPI` through the `pip` python package manager will not be covered here.

Run the `main.py` server and access the url  to see the message:
``` shell
# Run the server
cd ./learn/postgresql_crud/src/
./run.ps1

# Hit the endpoint
./learn/postgresql_crud/bat/get.bat
# Output: {"Hi":"World!"}
```

## Connection PostgreSQL Data

``` shell
python -m pip install psycopg2
```

In order to take the next simplest step, let's return data from our database. To prove we can do it, we will just fetch data from the `animal` table when we hit the `/` root path at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

To do this, we need to create a database connection. The database connection code can be defined in a python file called `database.py`. Create `src/config/database.py`. 

`learn/postgresql_crud/src/config/database.py`:
``` python
# TODO
```

TODO***

## API Design

Let's briefly design what our endpoints should be. 

We currently have three database tables: `animal`, `species`, `animal_species`. So for simplicity's sake, let's plan to have our API paths correspond to these tables:

Paths
* `/just_animals?{key1}={value1}&{key2}={value2}...{keyN}={valueN}` - just interacts with data from the animal table
* `/just_species?{key1}={value1}&{key2}={value2}...{keyN}={valueN}` - just interacts with data from the species table
* `/just_animal_species?{key1}={value1}&{key2}={value2}...{keyN}={valueN}` - just interacts with data from the animal_species table
* `/animals?{key1}={value1}&{key2}={value2}...{keyN}={valueN}` - used to get animal AND species data joined together

These different paths will allow filtering one or more database rows based on the `key/value` query string parameters tacked onto the end of the path. If no `key/value` parameters are provided, then ALL rows are selected. 

Different methods are used for different actions. Here are the methods that will be used for each endpoint:

* `GET` - retrieve data - allow filter query strings to get multiple items
* `POST` - add / modify data - only post one entity at a time (no query strings used to filter mulitple items)
* `DELETE` - delete data - allow filter query strings to delete multiple items

