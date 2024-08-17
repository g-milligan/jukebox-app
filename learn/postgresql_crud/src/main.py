from fastapi import FastAPI
import uvicorn
from entity.response import PostAnimalsResponse
from entity.request import PostAnimalRequest
from model.my_select import MySelect 
from model.my_add_update import MyAddUpdate 
from entity.data_tables import Animal, Species, AnimalSpecies

app = FastAPI()
select = MySelect()
add_update = MyAddUpdate()

# GET ALL

@app.get("/", response_model=list[Animal])
def root() -> list[Animal]:
    return select.get_animals()

@app.get("/all-animals", response_model=list[Animal])
def root() -> list[Animal]:
    return select.get_animals()

@app.get("/all-species", response_model=list[Species])
def root() -> list[Species]:
    return select.get_species()

@app.get("/all-animal-species", response_model=list[AnimalSpecies])
def root() -> list[AnimalSpecies]:
    return select.get_animal_species()

# POST

@app.post("/animals", response_model=PostAnimalsResponse)
def post_animal(animals: list[PostAnimalRequest]) -> PostAnimalsResponse:
    return add_update.add_animals(animals)





if __name__ == "__main__":
    # run this file through vscode to debug... 
    # python main.py 
    uvicorn.run(app, host="0.0.0.0", port=8000)