import trollius as asyncio

import time

import logging

logging.basicConfig()

clients = {}


def do_work():
    with open('/home/locke105/.vimrc') as vimrc:
        vimrc.read()

@asyncio.coroutine
def connect_client(client_reader, client_writer):
    task = asyncio.Task(serve_client(client_reader, client_writer))
    clients[task] = (client_reader, client_writer)

    def client_done(task):
        del clients[task]

    task.add_done_callback(client_done)

@asyncio.coroutine
def serve_client(client_reader, client_writer):
    print 'Handling client'
    client_writer.write("Hello")
    do_work()
    client_writer.write(" World!")
    client_writer.close()

loop = asyncio.get_event_loop()
server = loop.run_until_complete(
         asyncio.start_server(connect_client,
                              host='127.0.0.1',
                              port='8081'))
print 'Starting loop...'
loop.run_forever()
