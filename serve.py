#!/usr/bin/env python

import socket
import time
import datetime

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('localhost', 8081))

serversocket.listen(5)

while True:
    (clientsocket, address) = serversocket.accept()
    print str(datetime.datetime.now()) + " accepted conn"
    clientsocket.sendall('Hello')
    time.sleep(1)
    clientsocket.sendall(' World!')
    clientsocket.close()
    print str(datetime.datetime.now()) + " closed conn"
