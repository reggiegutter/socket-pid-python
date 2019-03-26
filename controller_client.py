"""Comparator Client for PID plant"""

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
TCP.connect((HOST, PORT))


def try_parse(text, fail=False):
    """Check numeral"""
    try:
        return float(text)
    except ValueError:
        return fail


print 'Use CTRL+X to quit\n'
MSG = raw_input()
while MSG <> '\x18':
    FLOAT_VAL = try_parse(MSG)

    if FLOAT_VAL is False:
        TO_SEND = "Enter a number"
    else:
        TO_SEND = str(FLOAT_VAL / 2)

    TCP.send(TO_SEND)
    MSG = raw_input()
TCP.close()
