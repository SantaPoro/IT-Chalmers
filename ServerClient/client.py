from multiprocessing import Process

import zmq
import random
import sys
import time
import sys

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]


name = input("Enter username: ")


print("Connecting to port: %s" % port)


context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
    msg = socket.recv()
    print(msg)
    send_this = input(":")

    if send_this == 'q':
        socket.send_string("QUIT")
        break

    socket.send_string("%s: %s" % (name, send_this))

    time.sleep(1)
