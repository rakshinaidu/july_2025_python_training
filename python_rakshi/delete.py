import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
cursor.execute("delete from users where id=3")
conn.commit()
conn.close()