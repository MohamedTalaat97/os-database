import zmq
from time import sleep
###########################################################
#defining port numbers port_1 --> master , port_2, port_3 -> slaves
port_1 = "5555"
port_2 = "5556"
port_3 ="5557"
###################################################SOCKETS
context_1 = zmq.Context()
socket_master = context_1.socket(zmq.REQ)
socket_master.connect ("tcp://localhost:%s" % port_1)
###############################################################################
context_2 = zmq.Context()
socket_2 = context_2.socket(zmq.REQ)
socket_2.connect ("tcp://localhost:%s" % port_2)
###########################################################
context_3 = zmq.Context()
socket_3 = context_3.socket(zmq.REQ)
socket_3.connect ("tcp://localhost:%s" % port_3)
#################################################33333
sockets=[]

sockets.append(socket_2)
sockets.append(socket_master)
sockets.append(socket_3)

#######################################################################
def sign_up(socket):
    #1- Ask user for data
      full_name = input("Enter your full name: ")
      email = input("Enter your email: ")
      address = input("Enter your address: ")
      password = input("Enter a password: ")
      #2- send user data to master
      data =[]
      data.append(full_name)
      data.append(email)
      data.append(address)
      data.append(password)
      data.append(1)
      socket.send_pyobj(data)
      #3- get reply from master
      message=socket.recv()
      print(message)
      return
###############################################################################
def sign_in(sockets):
      #1- Ask user for Authentication data 
      full_name = input("Enter your full name: ")
      password = input("Enter your password: ")
      email = "tempmail"
      address="tempaddress"
      #2- send retreive query to server and slaves 
      data =[]
      data.append(full_name)
      data.append(email)
      data.append(address)
      data.append(password)
      data.append(2)
      i=0
      while(1):
          sockets[i].send_pyobj(data)
          poller=zmq.Poller()
          poller.register(sockets[i],zmq.POLLIN)
          if (poller.poll(1*1000)):
              sleep(1)
              message= sockets[i].recv()
              print(message)
              break   
          else:
              if i == 2:
                  i=-1
          i+=1
                  
            
      return    
         
      
###############################################################################
def main():
  
    ###########################################################################
    #taking user request
    
    while(True):
       choice = input("To Sign_Up press 1 " + "To Sign_In press 2 \n")
       
       #processing user choice
       ########################################################################
       if choice == '1':
          sign_up(sockets[1])
       ######################################################################## 
       if choice == '2':
          sign_in(sockets)
  
###############################################################################
main()
      
    
    