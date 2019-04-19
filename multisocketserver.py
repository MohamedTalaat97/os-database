import zmq

port1 = "5559" 
context = zmq.Context()
print ("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port1)

print ("Sending request ")
socket.send_string ("Hello")
    #  Get the reply.
message = socket.recv()
