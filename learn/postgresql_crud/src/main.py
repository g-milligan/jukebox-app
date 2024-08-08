from fastapi import FastAPI
from model.my_query import MyQuery 
from entity.data_tables import Animal, Species, AnimalSpecies

app = FastAPI()
query = MyQuery()

@app.get("/", response_model=list[Animal])
def root() -> list[Animal]:
    return query.get_animals()