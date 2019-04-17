import zmq
port = "1111"
context_c = zmq.Context()
socket = context_c.socket(zmq.REP) 
socket.bind("tcp://*:%s" % port)



msg=socket.recv()
print(msg)
socket.send_string("rcv forom 1")

