from ..config.db_connection import DBConnection
import psycopg2

class MyDatabase:
    __connection = False

    def __init_connection(self):
        
        # if db connection is not already established
        if not self.__connection:
            
             config = DBConnection()
             
             # init connection once
             self.__connection = psycopg2.connect(
                database=config.getDBName(),
                user=config.getDBUser(),
                password=config.getDBSecret(),
                host=config.getDBHost(),
                port=config.getDBPort())
             
        # return the db connection
        return self.__connection

    def get_connection(self):
        return self.__init_connection()