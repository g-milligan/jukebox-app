from entity.data_tables import Animal, AnimalSpecies, Species
from . my_database import MyDatabase

class MyQuery:
    __connection = MyDatabase().get_connection()
    __cursor = __connection.cursor()
    
    def __run_query_all(self, sql_query):
        self.__cursor.execute(sql_query)
        print('Run query:', sql_query)
        return self.__cursor.fetchall()
    
    def get_animals(self) -> list[Animal]:
        animals = self.__run_query_all('SELECT * FROM animal')
        
        animal_list: list[Animal] = []
        for animal in animals:
            animal_list.append(Animal(animal))
            
        return animal_list
    
    def get_species(self) -> list[Species]:
        species = self.__run_query_all('SELECT * FROM species')
        
        species_list: list[Species] = []
        for item in species:
            species_list.append(Species(item))
            
        return species_list
    
    def get_animal_species(self) -> list[AnimalSpecies]:
        items = self.__run_query_all('SELECT * FROM animal_species')
        
        items_list: list[AnimalSpecies] = []
        for item in items:
            items_list.append(AnimalSpecies(item))
            
        return items_list
    
    