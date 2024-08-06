from fastapi import FastAPI
from model.my_query import MyQuery 

app = FastAPI()
query = MyQuery()

@app.get("/")
def root():
    return query.get_animals()