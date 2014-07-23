#!/usr/bin/env python

"""
Use with timeit module as follows::

    python -m timeit -n 10 'import map_client; map_client.main()'

Adjust -n 10 for the number of times you want to run the main() method.
"""


import multiprocessing
import os
import sys
import socket


def run(port):
    proc_num = os.getpid()

    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cs.connect(('127.0.0.1', int(port)))
    except socket.error:
        raise Exception("Proc %s - connection failed" % (proc_num))

    got_bytes = True
    mesg = ''
    while got_bytes:
        data = cs.recv(1024)
        if len(data) <= 0:
            got_bytes = False
        else:
            mesg += data

    cs.close()

    print 'Proc %s %s' % (proc_num, mesg)


def main():
    # run 500 client connections to the server at TCP port 8081
    num_procs = 500
    pool = multiprocessing.Pool()
    print 'Pool created.'
    work = [ 8081 for i in range(0, num_procs) ]
    pool.map_async(run, work)
    pool.close()
    pool.join()
    print 'Joined. Done.'


if __name__ == '__main__':
    main()
