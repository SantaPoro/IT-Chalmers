import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
    msg = socket.recv()
    print(msg)

    send_this = input(":")

    if send_this == 'q':
        break

    socket.send_string("client message: %s" % send_this)

    time.sleep(1)