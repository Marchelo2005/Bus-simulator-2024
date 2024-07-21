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
            if connection.is_connected():
                print("Connection to MySQL DB successful")
                myCursor = connection.cursor()
                sql = "INSERT INTO ACCOUNTINGTWO (totalPersons, totalMoney) VALUES (%s, %s)"
                insertValues = ("30", "12.5")
                myCursor.execute(sql, insertValues)
                connection.commit()  # Confirmar la transacción
                print(myCursor.rowcount, "registro insertado")
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if connection is not None and connection.is_connected():
                connection.close()
                print("MySQL connection is closed")
        return connection

# Llamada a la función create_connection
MyClass.create_connection(
    "mysql-esestrada.alwaysdata.net",
    "esestrada_machel",
    "W26y.yiJTxt!LLs",
    "esestrada_simula"
)
