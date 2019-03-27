"""Client for PID plant"""

import sys
import os

ARGUMENTS = sys.argv[1:]
COUNT = len(ARGUMENTS)

if COUNT != 2:
    print "Arguments required: HOST and PORT"
    exit()

HOST = ARGUMENTS[0]
PORT = int(ARGUMENTS[1])

CMD = 'python comparator.py ' + str(HOST) + ' ' + str(PORT) + ''
os.system(CMD)
