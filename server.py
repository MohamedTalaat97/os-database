import zmq
from time import sleep
import sqlite3 as lite

con = lite.connect('user.db')
cur = con.cursor() 
#####################################cleint port   
port = "5555"
context_c = zmq.Context()
socket_c = context_c.socket(zmq.REP) 
socket_c.bind("tcp://*:%s" % port)
##########################################slave Port
port_slaves = "3333" 
context_s = zmq.Context()
socket_s = context_s.socket(zmq.PUB) 
socket_s.bind("tcp://*:%s" % port_slaves)
###################################################
def sign_up(data):
    name = data[0];
    email = data[1];
    address = data[2];
    password = data[3];
    query1 = "select * from user where name = "+ "\""+name+"\""
    cur.execute (query1)
    check = cur.fetchall()
    print(check)
    reply=''
    if (cur.rowcount!=0):
       reply = 'user already exists'
    else :   
        query = "insert into user values (\""+name+ "\","+ "\""+email+"\","+"\""+address+"\","+"\""+password+"\")"
        cur.execute (query)
        con.commit()
        reply = 'sign up success'
        #socket_c.send_string("sign up successfully")
        print (data)
        #send to slaves
        socket_s.send_string(query)
    socket_c.send_string(reply) 
    sleep(1)
    return
############################################done
def sign_in(data):
    print("received data from sign in" , data)
    name = data[0];
    password = data[3];
    query = "select * from user where name ="+ "\""+name+"\""
    cur.execute (query)
    check = cur.fetchall()
    print(check)
    if (len(check) ==0):
       reply = 'user doesnt exist'
    else :
        if (check[0][3] == password):
            reply = 'sign in successfully!!'
        else:
            reply = 'incorrect passsowrd'    
    #socket_c.send_string("sign up successfully")
    print (data)
    socket_c.send_string(reply)
    #send to slaves
    sleep(1)
    return
             
##############################################

def main():
    
    while(1):
            print("---------------------")  
            data = socket_c.recv_pyobj()
            
            #sleep(10)
            if (data [4] == 1):
                sign_up(data)
            elif (data [4] == 2):
                sign_in(data)
                
                
        
           
            
main()