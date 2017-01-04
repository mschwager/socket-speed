#!/usr/bin/env python

import socket
import time

server_addr = '\0ans_server'

duration = 1
end = time.time() + duration
msgs = 0

print('Receiving messages...')

while time.time() < end:
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(server_addr)
    data = sock.recv(32)
    msgs += 1
    sock.close()

print('Received {} messages in {} second(s).'.format(msgs, duration))
