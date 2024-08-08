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

To do this, we need to create a database connection using python.

Creating a database connection in python requires us to make design decisions about how the code will be structured. For this connection, I will follow a folder structure using "model, entity and config" as folder names to help organize the different responsibilities of the python code:

* model - has the responsibility of interacting directly with the database. For example, any SQL query will be handled from within the "model" folder. This includes CRUD actions, performed by SQL queries
* entity - an entity represents a database table... for example the "animal" table can be mapped to an "Animal" dataclass in python. This sub-project has three main entities: `animal`, `species`, `animal_species` because these are the three tables in our database. There may be additional entities which represent individual data columns, as well. 
* config - this is where connection configuration can be stored. For example, the python code responsible for providing values for the database connection credentials can be written under this "config" folder. 

Here are the main files involved in interacting with the database:

* [src/config/db_connection.py](../src/config/db_connection.py) - Access database connection values (username, password, port, host, database-name) from either environment variables or hard-coded values
* [src/entity](../src/entity/) - All of the data entities will be defined under this folder. data entities are currently TBD at the time of this writing. First, the data will be accessed as raw values from the database. Later the raw values can be mapped to data entities to ensure the data adheres to expected typing.
* [src/model/my_database.py](../src/model/my_database.py) - this file establishes the connection to the database and handles potential errors. The python module `psycopg2` is used to establish the database connection. A `get_connection` method provides access to the established connection as a singleton object. "Singleton" means the object instance is only created once, even if the `get_connection` is called multiple times. 
* [src/model/my_query.py](../src/model/my_query.py) - The SQL queries are defined within this python file. This python file provides public methods used to perform the CRUD operations. 

Here is the result: The `my_query.py` module is imported into the `main.py` file and used to retrieve data from the `animal` table:

``` python
from fastapi import FastAPI
from model.my_query import MyQuery 

app = FastAPI()
query = MyQuery()

@app.get("/")
def root():
    # get animal data from the database
    return query.get_animals()
```

Now, when you hit the endpoint, `/`, you will see raw data being returned in the response, from the database!

Try it out by going to [http://localhost:8000/](http://localhost:8000/) or using the convenience script:

`[projectRoot]`
``` shell
.\learn\postgresql_crud\bat\get.bat        
```

You will see the output raw data coming from the database:
``` json
[
  [1, "Jerry",
    "jerry",
    16, false, "2024-08-04T00:05:36.344394",
    "2024-08-04T00:05:36.344394"
  ],
  [2, "Wilkinson Jimbo",
    "whyjimmy",
    44, true, "2024-08-04T00:05:36.344394",
    "2024-08-04T00:05:36.344394"
  ],
  [3, "Smifton Wuppledump",
    "smiffit",
    4, false, "2024-08-04T00:05:36.344394",
    "2024-08-04T00:05:36.344394"
  ],
  [4, "Tippy",
    "formerlylumpy",
    null, true, "2024-08-04T00:05:36.344394",
    "2024-08-04T00:05:36.344394"
  ],
  [5, "Clever Fred",
    "cled",
    90, false, "2024-08-04T00:05:36.344394",
    "2024-08-04T00:05:36.344394"
  ],
  [6, "Leon Regalion",
    "leonr",
    33, true, "2024-08-04T00:05:36.344394",
    "2024-08-04T00:05:36.344394"
  ],
  [7, "Noof Noof",
    "noofie",
    1030, false, "2024-08-04T00:05:36.344394",
    "2024-08-04T00:05:36.344394"
  ]
]
```

Note: If your database does not have this data, you must first complete the steps in the [previous tutorial](./01_postgresql_crud.md) which creates this data.

## Data Entities

Entities help guarantee raw data is stored using the expected format (with the correct fields and values). Entities represent the specific data shape. 

Each database table has its own "entity." In `python`, each "entity" can be defined with a `@dataclass`, which is a special type of python class that is meant to represent a data object. 

The `mydb_example` database entities have been created in this python file: [data_tables.py](../src/entity/data_tables.py)

The endpoint can be updated to require a response that returns a list of `Animal` entities:

``` python
from fastapi import FastAPI
from model.my_query import MyQuery 
from entity.data_tables import Animal

app = FastAPI()
query = MyQuery()

@app.get("/", response_model=list[Animal])
def root() -> list[Animal]:
    return query.get_animals()
```

Now the response from this endpoint will be structured following the `Animal` entity `@dataclass` structure:

``` json
[
  {
    "animal_id": 1,
    "animal_key": "jerry",
    "animal_created_at": "2024-08-04T00:05:36.344394",
    "animal_modified_at": "2024-08-04T00:05:36.344394",
    "animal_display_name": "Jerry",
    "animal_age": 16,
    "animal_is_friendly": false
  },
  {
    "animal_id": 2,
    "animal_key": "whyjimmy",
    "animal_created_at": "2024-08-04T00:05:36.344394",
    "animal_modified_at": "2024-08-04T00:05:36.344394",
    "animal_display_name": "Wilkinson Jimbo",
    "animal_age": 44,
    "animal_is_friendly": true
  },
  {
    "animal_id": 3,
    "animal_key": "smiffit",
    "animal_created_at": "2024-08-04T00:05:36.344394",
    "animal_modified_at": "2024-08-04T00:05:36.344394",
    "animal_display_name": "Smifton Wuppledump",
    "animal_age": 4,
    "animal_is_friendly": false
  },
  {
    "animal_id": 4,
    "animal_key": "formerlylumpy",
    "animal_created_at": "2024-08-04T00:05:36.344394",
    "animal_modified_at": "2024-08-04T00:05:36.344394",
    "animal_display_name": "Tippy",
    "animal_age": null,
    "animal_is_friendly": true
  },
  {
    "animal_id": 5,
    "animal_key": "cled",
    "animal_created_at": "2024-08-04T00:05:36.344394",
    "animal_modified_at": "2024-08-04T00:05:36.344394",
    "animal_display_name": "Clever Fred",
    "animal_age": 90,
    "animal_is_friendly": false
  },
  {
    "animal_id": 6,
    "animal_key": "leonr",
    "animal_created_at": "2024-08-04T00:05:36.344394",
    "animal_modified_at": "2024-08-04T00:05:36.344394",
    "animal_display_name": "Leon Regalion",
    "animal_age": 33,
    "animal_is_friendly": true
  },
  {
    "animal_id": 7,
    "animal_key": "noofie",
    "animal_created_at": "2024-08-04T00:05:36.344394",
    "animal_modified_at": "2024-08-04T00:05:36.344394",
    "animal_display_name": "Noof Noof",
    "animal_age": 1030,
    "animal_is_friendly": false
  }
]
```

## API Design

We have proven we can access data from our database through sending a request to one of our endpoints. 

Now, let's briefly design what our endpoints should be. 

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

