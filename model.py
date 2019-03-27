"""Comparator Client for PID plant"""

import socket
import sys
import os

ARGUMENTS = sys.argv[1:]
COUNT = len(ARGUMENTS)

if COUNT != 2:
    print "Arguments required: HOST and PORT"
    exit()

HOST = ARGUMENTS[0]
PORT = int(ARGUMENTS[1])

MAXSIZE = 1024

COMPARATOR = socket.socket()
COMPARATOR.connect((HOST, PORT))

MSG = raw_input('Model: ')
COMPARATOR.send(MSG)
FROM_SERVER = COMPARATOR.recv(MAXSIZE)

COMPARATOR.close()

print FROM_SERVER

CMD = 'python client.py ' + str(HOST) + ' ' + str(PORT) + ''
os.system(CMD)
