#!/usr/bin/env python

import socket

server_addr = '\0ans_server'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(server_addr)
sock.listen(0)

print('Server ready.')

while True:
    conn, _ = sock.accept()
    conn.send(b'Hello there!')
    conn.close()
