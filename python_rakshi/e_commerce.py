import sqlite3
conn=sqlite3.connect("e_commerce.db")
cursor=conn.cursor()
cursor.execute(
"CREATE TABLE if not exists Customer(id text not null,name text, email varchar,password int)")
cursor.execute("CREATE TABLE if not exists Orderdetails(cid integer,id integer,amount float,orderdate date)")
cursor.execute("CREATE TABLE if not exists Product(id integer not null ,name text,price float,description text )")
cursor.execute("CREATE TABLE if not exists Payment (id integer not null , type text,email varchar, password int)")
cursor.execute("CREATE TABLE if not exists Category(id integer not null ,name text,picture varchar, description text)")
cursor.execute("CREATE TABLE if not exists Cart(cartid integer not null,id integer not null)")
conn.commit()
conn.close()
