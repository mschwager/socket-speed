#!/usr/bin/env python

import os
import socket

server_addr = '/tmp/uds_server.sock'

if os.path.exists(server_addr):
    os.unlink(server_addr)

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(server_addr)
sock.listen(0)

print('Server ready.')

while True:
    conn, _ = sock.accept()
    conn.send(b'Hello there!')
    conn.close()
