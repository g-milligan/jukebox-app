from config.db_connection import DBConnection
import psycopg2

class MyDatabase:
    __connection = False

    def __init_connection(self):
        
        # if db connection is not already established
        if not self.__connection:
            print("Initializing connection to database...")
            
            config = DBConnection()
            
            try:
                # init connection once
                self.__connection = psycopg2.connect(
                database=config.getDBName(),
                user=config.getDBUser(),
                password=config.getDBSecret(),
                host=config.getDBHost(),
                port=config.getDBPort())
                
                print("Successfully connected to database!")
                
            except (Exception, psycopg2.Error) as error :
                print ("Error: Failed to connect to database.", error)
             
        # return the db connection
        return self.__connection

    def get_connection(self):
        return self.__init_connection()
    
    def close_connection(self):
        print("Close database connection...")
        
        if self.__connection:
            self.__connection.cursor().close()
            self.__connection.close()
            print("Database connection was closed.")
        else:
            print("Database connection already closed.")