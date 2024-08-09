from fastapi import FastAPI
import uvicorn
from entity.response import PostAnimalsResponse
from entity.request import PostAnimalRequest
from model.my_query import MyQuery 
from entity.data_tables import Animal, Species, AnimalSpecies

app = FastAPI()
query = MyQuery()

# GET ALL

@app.get("/", response_model=list[Animal])
def root() -> list[Animal]:
    return query.select.get_animals()

@app.get("/all-animals", response_model=list[Animal])
def root() -> list[Animal]:
    return query.select.get_animals()

@app.get("/all-species", response_model=list[Species])
def root() -> list[Species]:
    return query.select.get_species()

@app.get("/all-animal-species", response_model=list[AnimalSpecies])
def root() -> list[AnimalSpecies]:
    return query.select.get_animal_species()

# POST

@app.post("/animals", response_model=PostAnimalsResponse)
def post_animal(animals: list[PostAnimalRequest]) -> PostAnimalsResponse:
    return query.add_update.add_animals(animals)





if __name__ == "__main__":
    # run this file through vscode to debug... 
    # python main.py 
    uvicorn.run(app, host="0.0.0.0", port=8000)