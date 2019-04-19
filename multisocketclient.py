import zmq
from time import sleep

port2 = "5559"

context_m = zmq.Context()
socket_m = context_m.socket(zmq.REP) 
socket_m.bind("tcp://*:%s" % port2)

'''

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port2)

'''
message = socket_m.recv()
print (message)

socket_m.send_string("World from %s" % port2)

'''
msg=socket_m.recv()
socket_m.send_string("an el kbeer")
print(msg)
'''