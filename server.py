import zmq
from time import sleep
import sqlite3 as lite
from array import *
import threading 
######################################
con = lite.connect('user.db')
cur = con.cursor() 
#####################################cleint port   

port = "5555"
context_c = zmq.Context()
socket_c = context_c.socket(zmq.REP) 
socket_c.bind("tcp://*:%s" % port)

##########################################slave Ports --add port for each slave
port_slaves = "3333" 
context_s = zmq.Context()
socket_s = context_s.socket(zmq.REP) 
socket_s.bind("tcp://*:%s" % port_slaves)
#####################################socket array for slaves
slaveSockets =[]
slaveSockets.append(socket_s)
################################################### make 2-d array according to the number of slaves
nSlaves = 1 
slaves=[]
for i in range(nSlaves):
   
    arr=[]
    slaves.append(arr)
    
print(len(slaves))    
################################################### sign up function --it adds querys to slave arrays
def sign_up(data,cur,con):
    name = data[0];
    email = data[1];
    address = data[2];
    password = data[3];
    query1 = "select * from user where name = "+ "\""+name+"\""
    cur.execute (query1)
    check = cur.fetchall()
    print(check)
    reply=''
 
    if (len(check) != 0):
       reply = 'user already exists'
    else :   
        query = "insert into user values (\""+name+ "\","+ "\""+email+"\","+"\""+address+"\","+"\""+password+"\")"
        cur.execute (query)
        con.commit()
        reply = 'sign up success'
        print (data)
        #send to slaves
        for slave in slaves:
            slave.append(query)
    
    socket_c.send_string(reply) 
    sleep(1)
    return
############################################sign in function 
def sign_in(data,cur):
    print("received data from sign in" , data)
    name = data[0]
    password = data[3]
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
    print (data)
    socket_c.send_string(reply)
    return
############################################# slave thread 
def slaveThread(socket,i):
    #check on the slaves array 
    #if there data send to salves throug poling
    #if sent remevo it from array
    #if not keep it 
    #if array empty sent are you ready
    while(1):  
        message= socket.recv()
        print(message , "from slave")
        if (len(slaves[i])>0):
            socket.send_pyobj(slaves[i])
            slaves[i].clear()
                      
        else :
                message =[]
                message.append('9')
                socket.send_pyobj(message)
               
                sleep(1)
                
                     
##############################################
def clientThread():
    #wait on client 
    #execute
    con = lite.connect('user.db')
    cur = con.cursor()
    while(1):
        print("---------------------")  
        data = socket_c.recv_pyobj()    
        if (data [4] == 1):
            sign_up(data,cur,con)
        elif (data [4] == 2):
            sign_in(data,cur)
            
                
############################################ start of program
              
c1=threading.Thread(target = clientThread )
c2=threading.Thread(target = slaveThread,args = (slaveSockets[0],0) )  
             
                
c1.start()
c2.start()


c1.join()
c2.join()           
                
        
           
            