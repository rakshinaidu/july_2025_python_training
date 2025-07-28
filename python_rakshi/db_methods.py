import mysql.connector
def insert_data(id,name,password,email):
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


import mysql.connector
def update_data(name,id):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rakshi@05",
    database="rakshitha_cse"

    )
    cur=mydb.cursor()
    cur.execute("update user set name=%s where id=%s",(name,id))
    mydb.commit()
    cur.close()
    mydb.close()
    print("RECORD UPDATED.")


def deleteData():
import mysql.connector
def delete_data(id):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rakshi@05",
    database="rakshitha_cse"

    )
    cur=mydb.cursor()
    sql="delete from user where id=%s"
    val=(id,)
    cur.execute(sql,val)
    mydb.commit()
    cur.close()
   
    mydb.close()
    print("RECORD DELETED.")


import mysql.connector
def select_data():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rakshi@05",
    database="rakshitha_cse"

    )
    cur=mydb.cursor()
    sql="select * from user"
    cur.execute(sql)
    result=cur.fetchall()
    mydb.commit()
    cur.close()
    mydb.close()
    return result
  




    
