#!/usr/bin/env python

import socket

server_addr = '127.0.0.1'
server_port = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((server_addr, server_port))
sock.listen(0)

print('Server ready.')

while True:
    conn, _ = sock.accept()
    conn.send(b'Hello there!')
    conn.close()
