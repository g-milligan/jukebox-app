import os

class DBConnection:
    def getDBName(self):
        return 'mydb_example'
    
    def getDBHost(self):
        return 'localhost'
    
    def getDBPort(self):
        return 5432
    
    def getDBUser(self):
        return os.environ['DB_POSTGRESQL_USER']
    
    def getDBSecret(self):
        return os.environ['DB_POSTGRESQL_PWD']