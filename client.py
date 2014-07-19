#!/usr/bin/env python

import sys
import socket

port = sys.argv[2]

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cs.connect(('127.0.0.1', int(port)))
except socket.error:
    raise Exception("Proc %s - connection failed" % (sys.argv[1]))

got_bytes = True
mesg = ''
while got_bytes:
    data = cs.recv(1024)
    if len(data) <= 0:
        got_bytes = False
    else:
        mesg += data

cs.close()

print 'Proc %s %s' % (sys.argv[1], mesg)
