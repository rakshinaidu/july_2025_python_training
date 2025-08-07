from flask import Flask
app=Flask(__name__)

@app.route('/myname')
def myname():
    return 'Rakshitha Manjunath'

from flask import Flask, request,jsonify  
from flask_mysqldb import MySQL


app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="rakshi@05"
app.config['MYSQL_DB']="aug_cse"

mysql=MySQL(app)

@app.route('/select',methods=["GET"])
def register_save():
    
    # title=request.form.get("title")   
    # content=request.form.get("content")
    # json=request.get_json()
    # id=json.get("id")

    cur=mysql.connection.cursor()
    sql="select * from blog "
    cur=mysql.connection.cursor()
    cur.execute(sql)
    results=cur.fetchall()
    cur.close()
    return jsonify(results)

      




if __name__=='__main__':
    app.run() 