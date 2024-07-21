import mysql.connector
from mysql.connector import Error

class MyClass:
    @staticmethod
    def create_connection(host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection

# Crear la conexi�n
connection = MyClass.create_connection(
    "mysql-esestrada.alwaysdata.net", 
    "esestrada_machel", 
    "Paradais6666@.putini", 
    "esestrada_simula"
)

