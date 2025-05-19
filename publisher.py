import zmq
import time
import random
from constPS import *  # -

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://" + HOST + ":" + PORT   # how and where to communicate
s.bind(p)                          # bind socket to the address

while True:
    time.sleep(3)  # wait every 3 seconds

    # TIME topic
    msg_time = "TIME " + time.asctime()
    s.send_string(msg_time)

    # WELCOME topic
    msg_welcome = "WELCOME Bem-vindo ao sistema Pub/Sub!"
    s.send_string(msg_welcome)

    # TEMP topic (random temperature)
    temp = random.randint(20, 35)
    msg_temp = f"TEMP Temperatura atual: {temp}°C"
    s.send_string(msg_temp)