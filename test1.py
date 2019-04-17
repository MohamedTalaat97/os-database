import sqlite3 as lite

con = lite.connect('user.db')
cur = con.cursor() 
query = "create table user (name TEXT, email TEXT,address TEXT ,password TEXT)"
query2 = "select * from user"


cur.execute(query2)
print(cur.fetchall())


