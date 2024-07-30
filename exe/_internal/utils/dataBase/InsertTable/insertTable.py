import mysql.connector
from mysql.connector import Error
from utils.variables.variable.variable import variable
from utils.dataBase.connectorDb.connector_database import dataBase


def insertRecord(totalMoney):
        totalPersons = variable.passengerCounter
        connection = dataBase.createConnection()
        if connection:
            try:
                myCursor = connection.cursor()
                sql = "INSERT INTO busAccounting (totalPersons, totalMoney) VALUES (%s, %s)"
                insertValues = (totalPersons, totalMoney)
                myCursor.execute(sql, insertValues)
                connection.commit() 
                print(myCursor.rowcount, "record inserted")
            except Error as e:
                print(f"The error '{e}' occurred")
