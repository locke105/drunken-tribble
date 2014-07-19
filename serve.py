#!/usr/bin/env python

import socket
import time
import datetime

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('localhost', 8081))

serversocket.listen(100)

def do_work():
    with open('/home/locke105/.vimrc') as vimrc:
        vimrc.read()

while True:
    (clientsocket, address) = serversocket.accept()
    print str(datetime.datetime.now()) + " accepted conn"
    clientsocket.sendall('Hello')
    do_work()
    clientsocket.sendall(' World!')
    clientsocket.close()
    print str(datetime.datetime.now()) + " closed conn"
