from my_database import MyDatabase

class MyQuery:
    __connection = MyDatabase().get_connection()
    pass