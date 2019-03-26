"""Comparator Server for PID plant"""

import socket
import sys

ARGUMENTS = sys.argv[1:]
COUNT = len(ARGUMENTS)

if COUNT != 2:
    print "Arguments required: HOST and PORT"
    exit()

HOST = ARGUMENTS[0]
PORT = int(ARGUMENTS[1])

TCP = socket.socket()
TCP.bind((HOST, PORT))
TCP.listen(5)

while True:
    CON, CLIENT = TCP.accept()
    print 'Connected by', CLIENT
    while True:
        MSG = CON.recv(1024)
        if not MSG:
            break
        print CLIENT, MSG
    print 'Closing connection with client', CLIENT
    CON.close()
    exit()
