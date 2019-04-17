import zmq
from time import sleep
port = "1111"
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

'''
port = "1111"
context = zmq.Context()
socket_1 = context.socket(zmq.REQ)
socket_1.connect ("tcp://localhost:%s" % port)
'''

socket.send_string("socket 1")
poller=zmq.Poller()
poller.register(socket,zmq.POLLIN)
while(1):
    if (poller.poll(1*1000)):
        sleep(1)
        message= socket.recv()
        print(message) 
    else :print("sent failed , retrying")


'''
socket_1.send_string("socket 2")
msg=socket_1.recv()
print(msg)
'''