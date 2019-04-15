import zmq
from time import sleep
import threading


port = "5555"
context = zmq.Context()
socket = context.socket(zmq.REP) 
socket.bind("tcp://*:%s" % port)


def execute():

    message =[1]
    socket.send_pyobj(message)
    print("hello from thread !!!!!!")
    data =[]
    data = socket.recv_pyobj()
    #construct query here
    print (data)
    socket.send_string("sign up successfully")


    

def main():
    
    while(1):
            data = socket.recv_pyobj()
            #construct query here
            print (data)
            socket.send_string("sign up successfully")

        


             
             
main()