import zmq
from time import sleep

port_m = "5559"
context_m = zmq.Context()
socket_m = context_m.socket(zmq.REP) 
socket_m.bind("tcp://*:%s" % port_m)







msg=socket_m.recv()
socket_m.send_string("an el kbeer")
print(msg)
