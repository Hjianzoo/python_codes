#!/usr/bin/python
#coding:utf-8 
#

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re

myfile = open('hilink_ac_0045.key','rb')
out_file = open ('hilink_key.txt','w')
line_count = 0;
while True:
	line = myfile.readline()
	if not line:
		break
	print len(line)
	for i in range(0,len(line)):
		byte = ord(line[i])
		print hex(byte)
		out_file.write(hex(byte))
		out_file.write(',')
		line_count +=1
		if line_count%16 == 0 :
			out_file.write('\n')
out_file.close()
myfile.close()
