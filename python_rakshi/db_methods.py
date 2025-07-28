# import mysql.connector
# def insert_data(id,name,password,email):
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rakshi@05",
#     database="rakshitha_cse"

#     )
#     cur=mydb.cursor()
#     sql="INSERT INTO user (id,name,password,email) VALUES (%s,%s,%s,%s)"
#     val=(id,name,password,email)
#     cur.execute(sql,val)
#     mydb.commit()
#     cur.close()
   
#     mydb.close()
#     print("RECORD INSERTED.")


# def updateData():
import mysql.connector
def updat_data(id,name,password,email):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rakshi@05",
    database="rakshitha_cse"

    )
    cur=mydb.cursor()
    sql="INSERT INTO user (id,name,password,email) VALUES (%s,%s,%s,%s)"
    val=(id,name,password,email)
    cur.execute(sql,val)
    mydb.commit()
    cur.close()
   
    mydb.close()
    print("RECORD INSERTED.")


# def deleteData():

# def selectData():

    
