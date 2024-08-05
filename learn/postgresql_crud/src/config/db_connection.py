import os

class DBConnection:
    def getDBName():
        return 'mydb_example'
    
    def getDBHost():
        return 'localhost'
    
    def getDBPort():
        return 5432
    
    def getDBUser():
        return os.environ['DB_POSTGRESQL_USER']
    
    def getDBSecret():
        return os.environ['DB_POSTGRESQL_PWD']