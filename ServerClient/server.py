from multiprocessing import Process

import zmq
import random
import sys
import time
import multiprocessing
import threading


def take_input():
    print("Take_Input")
    while True:
        input("Skriv: ")


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)

        while True:
            print("Running: " + self.name)
            take_input()

        # print("Exiting " + self.name)


thread1 = MyThread(1, "Thread take input", 1)
thread1.start()

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]

print("Listening to port: %s" % port)


def main_loop():
    print("main_loop")
    while True:
        socket.send_string("Server message to client3")
        msg = socket.recv().decode()
        if msg == "QUIT":
            print("Quitting server!")
            break

        print(msg)
        time.sleep(1)


context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)


main_loop()
