#

import socket
import json
 
"""
A simple python server that uses this api:
https://github.com/happyleavesaoc/python-orvibo
To send on/off signals to the orbivo s20 wifi smart switch
 
TODO:
* simple android app to send messages over the internet from phone
* setup dynamic dns and port forwarding for this server on nas
 
"""
 
def isStatusRequest(message):
    return message == 'status'
 
def getStatusString():
    return json.dumps({'plug1': plug1, 'plug2': plug2})
 
def getPlugOnOff(plug):
    return 'on' if plug else 'off'
 
 
plug1 = False
plug2 = False
 
host = ''
port = 50000
backlog = 5
size = 1024
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
 
while 1:
    client, address = s.accept()
    #print 'Got connection from', address
    data = client.recv(size)
    #print 'Got message: ', data
 
    if isStatusRequest(data):
        client.send(getStatusString())
        print "Got status request, sending: ", getStatusString()
    else:
        # we want to turn on or off one of the plugs
        if(data == 'plug1'):
            plug1 = not plug1
            print 'Turning plug1 ', getPlugOnOff(plug1)
        if(data == 'plug2'):
            plug2 = not plug2
            print 'Turning plug2 ', getPlugOnOff(plug2)
 
    client.close()
