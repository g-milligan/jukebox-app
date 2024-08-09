from entity.response import PostAnimalsResponse, ResponseSummary
from entity.request import PostAnimalRequest
from entity.response import PostAnimalsResponse

class MyAddUpdate:
    def __init__(self, cursor) -> None:
        self.__cursor = cursor
        
    def __run_insert(self, sql_query):
        result = self.__cursor.execute(sql_query)
        print('Run insert:', sql_query)
        return result
        
    def add_animals(self, animals: list[PostAnimalRequest]) -> PostAnimalsResponse:
        columns = [
            'animal_display_name', 
            'animal_key', 
            'animal_age', 
            'animal_is_friendly'
        ]
        build_query = 'INSERT INTO animal(' + ','.join(columns) + ') VALUES'
        
        r = 0
        for animal in animals:
            if r != 0:
                build_query += ","
            build_query += "("
            
            build_query += f"'{animal.animal_display_name}',"
            build_query += f"'{animal.animal_key}',"
            build_query += f"{animal.animal_age},"
            build_query += f"{animal.animal_is_friendly}"
            
            build_query += ")"
            r+=1
            
        build_query += ";"
        
        result = self.__run_insert(build_query)
        
        print('RESULT: ', result)
        
        return PostAnimalsResponse(
            summary=ResponseSummary(
                status_code=200, 
                status_label="OK", 
                message=""
            )
        )