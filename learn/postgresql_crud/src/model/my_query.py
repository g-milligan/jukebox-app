from model.my_add_update import MyAddUpdate
from model.my_select import MySelect
from . my_database import MyDatabase

class MyQuery:
    __connection = MyDatabase().get_connection()
    __cursor = __connection.cursor()
    
    select = MySelect(__cursor)
    add_update = MyAddUpdate(__cursor)

    
    