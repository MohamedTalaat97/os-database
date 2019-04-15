import zmq
import time

###############################################################################
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
      socket.send_pyobj(data)
      #3- get reply from master


      reply= socket.recv()
      print("ay7aga")
      print("reply from server ", reply)
      return
###############################################################################
def sign_in(socket):
      #1- Ask user for Authentication data 
      full_name = input("Enter your full name: ")
      password = input("Enter your password: ")
      #2- send retreive query to server and slaves 
      data =[]
      data.append(full_name)
      data.append(password)
      socket.send_pyobj(data)
      #3- get reply from server and slaves
      reply = socket.recv()    
      print("reply from server ", reply)

      
      #3- if user not exist 
      # ask user to sign up
      
      #4- if user exit verify password
      
      #5- if correct password print sign in successfully
      
      #6- if wrong password print incorrect password
      return    
         
      
    

    

###############################################################################
def delete_account(socket_master):
    #1- sign_in
    sign_in()
    #2- send delete query to master
    socket_master.send ("Delete query")
    #3 receiving reply form master
    reply_master = socket_master.recv()
    print("reply from master "+ reply_master)
    return
###############################################################################
def main():
    #defining port numbers port_1 --> master , port_2, port_3 -> slaves
    port_1 = "5555"
    port_2 = "5556"
    port_3 = "5557"
    
    #connecting to master and slaves
    context = zmq.Context()
    print ("Connecting to Master...")
    socket_master = context.socket(zmq.REQ)
    '''
    socket_slave_1 = context.socket(zmq.REQ)
    socket_slave_2 = context.socket(zmq.REQ)
    '''
    socket_master.connect ("tcp://localhost:%s" % port_1)
    socket_master.connect ("tcp://localhost:%s" % port_2)
    socket_master.connect ("tcp://localhost:%s" % port_3)
    print ("Connecting to Slaves...")
    '''
    socket_slave_1.connect ("tcp://localhost:%s" % port_2)
    socket_slave_2.connect ("tcp://localhost:%s" % port_3)
    '''
    ###########################################################################
    #taking user request
    
    while(True):
       choice = input("To Sign_Up press 1 " + "To Sign_In press 2 " + "To Delete your account press 3 \n")
       
       #processing user choice
       ########################################################################
       if choice == '1':
          #poll to see if master is ready
          socket = None 
          #sign_up
          sign_up(socket_master)
       ######################################################################## 
       if choice == '2':
          #poll to see if any sever is ready
          socket = None 
          while True:
              try:
                 socket_master.send_string ("Are You Ready !!",flags=zmq.NOBLOCK)
                 time.sleep(1)
                 reply_master=socket_master.recv(flags=zmq.NOBLOCK)
                 print ("received " , reply_master ," from master")
                 if int(reply_master) == 1:
                     socket= socket_master
                     break
              except zmq.Again as e:
                 e="Master is busy right now !!"
                 print(e)
              try:
                 socket_slave_1.send_string ("Are You Ready !!",flags=zmq.NOBLOCK)
                 time.sleep(1)
                 reply_slave=socket_slave_1.recv(flags=zmq.NOBLOCK)
                 print ("received " ,reply_slave," from slave_1")
                 if int(reply_slave) == 1:
                     socket= socket_slave_1
                     break
              except zmq.Again as e:
                 e="slave_1 is busy right now !!"
                 print(e)             
              try:
                 socket_slave_2.send_string ("Are You Ready !!",flags=zmq.NOBLOCK)
                 time.sleep(1)
                 reply_slave=socket_slave_2.recv(flags=zmq.NOBLOCK)
                 print ("received " ,reply_slave," from master")
                 if int(reply_slave) == 1:
                     socket= socket_slave_2
                     break
              except zmq.Again as e:
                 e="slave_2 is busy right now !!"
                 print(e)
                 

                  
                  
          
                 
          #sign_in
          sign_in(socket)
       if choice == '3':
          #Delete account
          delete_account(socket_master)
       
      
    
###############################################################################
main()
      
    
    