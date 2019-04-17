import zmq
from time import sleep
import sqlite3 as lite
import threading 
#################################cleint
port_c = "5556"
context_c = zmq.Context()
socket_c = context_c.socket(zmq.REP) 
socket_c.bind("tcp://*:%s" % port_c)
####################################master
port_m = "3333"
context_m = zmq.Context()
socket_m = context_m.socket(zmq.SUB) 
socket_m.bind("tcp://localhost:%s" % port_c)
##################################

def cleint(query):
      query = socket_c.recv_pyobj()
      cur.execute(query)
      
def master(query):
      query = socket_m.recv_pyobj()
      cur.execute(query)      

##########################################################

con = lite.connect('user.db')
cur = con.cursor()


def main():
    
    while(1):
          threading.Thread(target = master).start()
          threading.Thread(target = master).start()
          
          
main()