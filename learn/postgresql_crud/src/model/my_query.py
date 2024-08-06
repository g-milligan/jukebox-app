from . my_database import MyDatabase

class MyQuery:
    __connection = MyDatabase().get_connection()
    __cursor = __connection.cursor()
    
    def get_animals(self):
        sql_query = 'SELECT * FROM animal'
        self.__cursor.execute(sql_query)
        print('Run query:', sql_query)
        return self.__cursor.fetchall()
    
    