import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
c=int(input("Enter the number of users:"))
for i in range(c):
    n=input("Enter the name:")
    a=int(input("Enter the age:"))
    cursor.execute("INSERT INTO users (name,age) VALUES(?,?)",(n,a))
conn.commit()
conn.close()



