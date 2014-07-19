#!/usr/bin/env python

import socket
import time
import datetime
import select

in_sockets = []
out_sockets = []

def handle_client(clientsocket):
    clientsocket.sendall('Hello')
    time.sleep(1)
    clientsocket.sendall(' World!')
    clientsocket.close()
    print str(datetime.datetime.now()) + " closed conn"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# async
serversocket.setblocking(0)

serversocket.bind(('localhost', 8082))

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
