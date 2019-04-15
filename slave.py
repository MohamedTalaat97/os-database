import zmq



def main():
    port = "5556"
    context = zmq.Context()
    socket = context.socket(zmq.PAIR) 
    socket.bind("tcp://*:%s" % port)
    
    
    while True:
        try:
            #check for a message, this will not block
            message = socket.recv(flags=zmq.NOBLOCK)
            #a message has been received
            print ("received:", message , "from client")
            socket.send_string("1")
            break
        except zmq.Again as e:
            e="No requests yet !!"
            print( e)
    
    data =[]    
    data = socket.recv_pyobj()
    print("received user data in master ",data)
    socket.send_string("sign in successfully")
    
             
             
main()