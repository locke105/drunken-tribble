#!/usr/bin/env python

import socket
import time
import datetime
import select

in_sockets = []
out_sockets = []

def do_work():
    with open('/home/locke105/.vimrc') as vimrc:
        vimrc.read()

def handle_client(clientsocket):
    clientsocket.sendall('Hello')
    do_work()
    clientsocket.sendall(' World!')
    clientsocket.close()
    print str(datetime.datetime.now()) + " closed conn"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# async
serversocket.setblocking(0)

serversocket.bind(('localhost', 8081))

serversocket.listen(5)

in_sockets.append(serversocket)

while True:
    ins, outs, errs = select.select(in_sockets, out_sockets, [], 60)

    for in_sock in ins:
        (clientsocket, address) = serversocket.accept()
        clientsocket.setblocking(0)
        print str(datetime.datetime.now()) + " accepted conn"
        out_sockets.append(clientsocket)

    for out_sock in outs:
        handle_client(out_sock)
        out_sockets.remove(out_sock)
