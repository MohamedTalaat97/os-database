import zmq

port_slaves = "5559" 
context_s = zmq.Context()
socket_s = context_s.socket(zmq.REQ) 
socket_s.bind("tcp://localhost:%s" % port_slaves)



socket_s.send_string("master")


msg=socket_s.recv()