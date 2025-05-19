import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")

for i in range(5):
    msg = s.recv()
    print("TIME:", msg.decode())