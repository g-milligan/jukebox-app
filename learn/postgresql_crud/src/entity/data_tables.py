
from dataclasses import dataclass
import datetime
from enum import Enum

@dataclass
class Animal:
    animal_id: int
    animal_key: str
    animal_created_at: datetime.datetime
    animal_modified_at: datetime.datetime
    animal_display_name: str = ''
    animal_age: int = -1
    animal_is_friendly: bool = False
    def __init__(self, thing = False):
        if not thing:
            return
        # class_attrs = list(filter(lambda key : not key.startswith('_'), dir(self)))
        # print('TESTING: ', class_attrs)
        self.animal_id = thing[0]
        self.animal_display_name = thing[1]
        self.animal_key = thing[2]
        self.animal_age = thing[3]
        self.animal_is_friendly = thing[4]
        self.animal_created_at = thing[5]
        self.animal_modified_at = thing[6]
    
class VoreType(Enum):
    UNKOWN = 'Unknown'
    CARNIVORE = 'Carnivore'
    HERBIVORE = 'Herbivore'
    OMNIVORE = 'Omnivore'
    
@dataclass
class Species:
    species_id: int
    species_key: str
    species_created_at: datetime.datetime
    species_modified_at: datetime.datetime
    species_display_name: str = ''
    species_vore_type: VoreType = VoreType.UNKOWN
    def __init__(self, thing = False):
        if not thing:
            return
        self.species_id = thing[0]
        self.species_display_name = thing[1]
        self.species_key = thing[2]
        self.species_vore_type = thing[3]
        self.species_created_at = thing[4]
        self.species_modified_at = thing[5]
    
@dataclass
class AnimalSpecies:
    animal_species_id: int
    fk_species_id: int
    fk_animal_id: int
    animal_species_created_at: datetime.datetime
    animal_species_modified_at: datetime.datetime
    def __init__(self, thing = False):
        if not thing:
            return
        self.animal_species_id = thing[0]
        self.fk_species_id = thing[1]
        self.fk_animal_id = thing[2]
        self.animal_species_created_at = thing[3]
        self.animal_species_modified_at = thing[4]
    
@dataclass
class CombinedAnimalSpecies:
    species: Species
    animal: Animal
    animal_species: AnimalSpecies
    def __init__(self, species: Species, animal: Animal, animal_species: AnimalSpecies):
        self.species = species
        self.animal = animal
        self.animal_species = animal_species