
import mysql.connector
def getDb():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="rakshi@05",
    database="rakshitha_cse"
    )
    return mydb
