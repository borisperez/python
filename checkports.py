# To execute this python command:
# python checkports.py [sever_name | server_IP] "port1,port2,port3,port4"

import socket
import sys

host = sys.argv[1]
portList = sys.argv[2].split(",")

print "Check open ports on Host: " + host
while portList:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    port = int(portList.pop())
    result = sock.connect_ex((host,port))
    if result == 0:
       print "Port: " + str(port) + " is Open"
    else:
       print "Port: " + str(port) + " is Close or listening services is down!"
sock.close()