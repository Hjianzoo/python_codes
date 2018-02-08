#!/usr/bin/python
#coding:utf-8 
 
import socket   #for sockets
 
try:
#create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error, msg:
	print 'failed to create socket,Error code :'+ str(msg[0])+',error message: ' + msg[1]
	sys.exit();

print 'Socket Created'

host = 'api.easylink.io'
port = 80

try:
	remote_ip = socket.gethostbyname(host)

except socket.gaierror:
	print 'hostname could not be resolved.Exiting'
	sys.exit()
print 'Ip address of ' + host + ' is ' + remote_ip

s.connect((remote_ip,port))
print 'socket connected to ' + host + 'on ip '+ remote_ip

message = "GET http://api.easylink.io/roms/d3cb8d731b9f11b8f58b1a17631fc365.bin HTTP/1.1\r\nHost:new.qq.com\r\nConnection:keep-alive\r\n\r\n"
try:
	s.sendall(message)
except socket.error:
	print 'send failed'
	sys.exit()
print 'message send successfully'
reply = ''
s.settimeout(1)
temp = s.recv(1024)
for i in range(1,35):
	print i
	reply += temp;
	temp = s.recv(1024)
	if not len(temp):
		break




fp = open('download_test.txt','w+')
fp.write(reply +'\n')
fp.close()
#print temp.json()

#print reply
print '*********************************************************\r\n'

#str = ''#'GET / HTTP/1.1'+'Host: www.baidu.com'+'Connection: keep-alive'\




#s.send(str)
