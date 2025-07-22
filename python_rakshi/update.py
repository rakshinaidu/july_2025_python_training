import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
cursor.execute("update users set name='SARA' where id=1")
cursor.execute("update users set name='JUNNU' where id=4")
cursor.execute("update users set age=22 where id=4")
cursor.execute("update users set age=23 where id=2")
conn.commit()
conn.close()
