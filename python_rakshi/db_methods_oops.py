from db_lib import getDb

class classMethods:
    def insert_data(self,id,name,password,email):
        mydb=getDb()
        cur=mydb.cursor()
        sql="INSERT INTO user (id,name,password,email) VALUES (%s,%s,%s,%s)"
        val=(id,name,password,email)
        cur.execute(sql,val)
        mydb.commit()
        cur.close()
    
        mydb.close()
        print("RECORD INSERTED.")


    def update_data(self,name,id):
        mydb=getDb()
        cur=mydb.cursor()
        cur.execute("update user set name=%s where id=%s",(name,id))
        mydb.commit()
        cur.close()
        mydb.close()
        print("RECORD UPDATED.")


    def delete_data(self,id):
        mydb=getDb()
        cur=mydb.cursor()
        sql="delete from user where id=%s"
        val=(id,)
        cur.execute(sql,val)
        mydb.commit()
        cur.close()
    
        mydb.close()
        print("RECORD DELETED.")


    def select_data(self):
        mydb=getDb()
        cur=mydb.cursor()
        sql="select * from user"
        cur.execute(sql)
        result=cur.fetchall()
        mydb.commit()
        cur.close()
        mydb.close()
        return result
    




        
