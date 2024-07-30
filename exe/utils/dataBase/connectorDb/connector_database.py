import mysql.connector
from mysql.connector import Error
class dataBase:
    connection = None
    def createConnection():
        try:
            connection = mysql.connector.connect(
                host="mysql-esestrada.alwaysdata.net",
                user="esestrada_machel",
                passwd="W26y.yiJTxt!LLs",
                database="esestrada_simula"
            )
            if connection.is_connected():
                print("Connection to the database was successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection
