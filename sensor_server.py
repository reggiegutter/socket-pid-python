"""Sensor Server for PID plant"""

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

# while True:
#     recebido = addr.recv(4096)
#     print recebido.find("sair")
#     if (recebido == "sair"):
#         print "Solicitado saida!"
#         break
#     print "recebido:[", float(recebido) / 2, "]"
#     addr.send(recebido)

# sc.close()
# client.close()


# from simple_pid import PID
# pid = PID(1, 0.1, 0.05, setpoint=1)

# # assume we have a system we want to control in controlled_system
# v = controlled_system.update(0)

# while True:
#     # compute new ouput from the PID according to the systems current value
#     control = pid(v)

#     # feed the PID output to the system and get its current value
#     v = controlled_system.update(control)
