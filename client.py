#! /usr/bin/env python
import socket
 
 
while True:
    cmd=raw_input("cmd: ")
    if cmd == 'exit':
        break
    else:
        s = socket.socket()
        host = socket.gethostname()
        port=50000
        s.connect((host, port))
        s.send(cmd)
 
        if cmd == 'status':
            print s.recv(1024)
 
        s.close()
