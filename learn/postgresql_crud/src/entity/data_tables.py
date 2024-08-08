
from dataclasses import dataclass
import datetime
from enum import Enum

class TableBase:
    def default_if_none(self, type, value, default_value):
        if (value is None):
            return default_value
        
        return type(value)
        
    def map_to_self(self, class_name, values = [], column_names: list[str] = []):
        if not values:
            return
        
        columns_size = len(column_names)
        values_size = len(values)
        
        if columns_size != values_size:
            raise Exception(f'{class_name}: Cannot map column size({columns_size}) to value size({values_size}) column_names({column_names}) values({values})')
        
        i = 0
        for nameFunc in column_names:
            setattr(self, nameFunc[0], nameFunc[1](values[i]))
            i += 1

@dataclass
class Animal(TableBase):
    animal_id: int
    animal_key: str
    animal_created_at: datetime.datetime
    animal_modified_at: datetime.datetime
    animal_display_name: str = ''
    animal_age: int = -1
    animal_is_friendly: bool = False
    def __init__(self, thing = False):
        self.map_to_self(
            'Animal', thing,
            [ 
            ('animal_id', lambda i : int(i)), 
            ('animal_display_name', lambda i : self.default_if_none(str, i, '')), 
            ('animal_key', lambda i : str(i)), 
            ('animal_age', lambda i : self.default_if_none(int, i, -1)), 
            ('animal_is_friendly', lambda i : self.default_if_none(bool, i, False)), 
            ('animal_created_at', lambda i : i), 
            ('animal_modified_at', lambda i : i),
            ])
    
class VoreType(Enum):
    UNKNOWN = 'Unknown'
    CARNIVORE = 'Carnivore'
    HERBIVORE = 'Herbivore'
    OMNIVORE = 'Omnivore'
    
@dataclass
class Species(TableBase):
    species_id: int
    species_key: str
    species_created_at: datetime.datetime
    species_modified_at: datetime.datetime
    species_display_name: str = ''
    species_vore_type: VoreType = VoreType.UNKNOWN
    def __init__(self, thing = False):
        self.map_to_self(
            'Species', thing,
            [
            ('species_id', lambda i : int(i)),
            ('species_display_name', lambda i : self.default_if_none(str, i, '')),
            ('species_key', lambda i : str(i)),
            ('species_vore_type', lambda i : self.default_if_none(VoreType, i, VoreType.UNKNOWN)), 
            ('species_created_at', lambda i : i), 
            ('species_modified_at',  lambda i : i),
            ])
    
@dataclass
class AnimalSpecies(TableBase):
    animal_species_id: int
    fk_species_id: int
    fk_animal_id: int
    animal_species_created_at: datetime.datetime
    animal_species_modified_at: datetime.datetime
    def __init__(self, thing = False):
        self.map_to_self(
            'AnimalSpecies', thing,
            [
            ('animal_species_id', lambda i : int(i)),
            ('fk_species_id', lambda i : int(i)), 
            ('fk_animal_id', lambda i : int(i)),
            ('animal_species_created_at', lambda i : i), 
            ('animal_species_modified_at', lambda i : i),
            ])
    
@dataclass
class CombinedAnimalSpecies:
    species: Species
    animal: Animal
    animal_species: AnimalSpecies
    def __init__(self, species: Species, animal: Animal, animal_species: AnimalSpecies):
        self.species = species
        self.animal = animal
        self.animal_species = animal_species