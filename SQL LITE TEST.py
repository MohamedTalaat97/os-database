import sqlite3 as lite

con = lite.connect('user.db')
cur = con.cursor()

def sign_up(data):
    name = data[0];
    email = data[1];
    address = data[2];
    password = data[3];
    #query = "insert into user values ("+name+ ","+email+","+address+","+password =")"
    query = "insert into user values (\""+name+ "\","+ "\""+email+"\","+"\""+address+"\","+"\""+password+"\")"
    cur.execute (query)
    con.commit()
    

data = ['rrrrrrrrrrrrrrr','fgg','fdf','ddf']
name = data[0];
email = data[1];
address = data[2];
password = data[3];
query = "insert into user values (\""+name+ "\","+ "\""+email+"\","+"\""+address+"\","+"\""+password+"\")"
cur.execute (query)
d = cur.fetchall()
if (d == None):
    print ('awesome')