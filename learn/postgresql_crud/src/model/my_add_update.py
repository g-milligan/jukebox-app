import datetime
import uuid
from entity.response import PostAnimalsResponse, ResponseSummary
from entity.request import PostAnimalRequest
from entity.response import PostAnimalsResponse
from entity.data_tables import Animal
from model.my_database import MyDatabase

class MyAddUpdate:
    def __init__(self) -> None:
        self.__connection = MyDatabase().get_connection()
        self.__cursor = self.__connection.cursor()
        
    def __run_insert(self, sql_query):
        try:
            self.__cursor.execute(sql_query)
            print('Run insert:', sql_query)
            
            # commit changes to the database
            self.__connection.commit() 
            
            return (200, 'OK', 'Success: new items added')
        except(Exception) as error:
            print('Error insert:', error)
            
            # reset cursor
            self.__cursor.close()
            self.__connection.close()
            self.__connection = MyDatabase().get_connection()
            self.__cursor = self.__connection.cursor()
            
            return (500, 'Internal Server Error', f'ERROR: {error}')
    
    def add_animals(self, animals: list[PostAnimalRequest]) -> PostAnimalsResponse:
        columns = [
            'animal_display_name', 
            'animal_key', 
            'animal_age', 
            'animal_is_friendly',
            'animal_created_at',
            'animal_modified_at'
        ]
        build_query = 'INSERT INTO animal(' + ','.join(columns) + ') VALUES'
        
        added_animals: list[Animal] = []        
        r = 0
        for animal in animals:
            if r != 0:
                build_query += ","
            build_query += "("
            
            nowtime = datetime.datetime.now(datetime.timezone.utc)
            animal_key = animal.animal_key
            if animal_key == None:
                animal_key = uuid.uuid4()
            
            added_animal = Animal([ # ughhhh missing primary id key.... need to find a better way to map entities
                animal.animal_display_name,
                animal_key,
                animal.animal_age,
                animal.animal_is_friendly,
                nowtime,
                nowtime
            ])
            added_animals.append(added_animal)
            
            build_query += f"'{added_animal.animal_display_name}',"
            build_query += f"'{added_animal.animal_key}',"
            build_query += f"{added_animal.animal_age},"
            build_query += f"{added_animal.animal_is_friendly},"
            build_query += f"'{added_animal.animal_created_at}',"
            build_query += f"'{added_animal.animal_modified_at}'"
            
            build_query += ")"
            r+=1
            
        build_query += ";"
        
        status_code, status_label, message = self.__run_insert(build_query)
        
        return PostAnimalsResponse(
            summary=ResponseSummary(
                status_code=status_code, 
                status_label=status_label, 
                message=message
            ),
            animals=added_animals
        )