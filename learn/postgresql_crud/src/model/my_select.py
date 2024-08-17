from entity.data_tables import Animal, AnimalSpecies, Species
from model.my_database import MyDatabase

class MySelect:
    def __init__(self) -> None:
        self.__connection = MyDatabase().get_connection()
        self.__cursor = self.__connection.cursor()

    def __run_query_all(self, sql_query):
        try:
            self.__cursor.execute(sql_query)
            print('Run select all:', sql_query)
            return self.__cursor.fetchall()
        except(Exception) as error:
            print('Error select all:', error)
            
            # reset cursor
            self.__cursor.close()
            self.__connection.close()
            self.__connection = MyDatabase().get_connection()
            self.__cursor = self.__connection.cursor()
    
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