#!/usr/bin/python  
#coding:utf-8 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


fr = open('content.txt','r')

characers = []
stat = {}

for line in fr:
	line = line.strip()
	if len(line) == 0:
		continue
	print type(line)
	#line.decode("utf-8")
	#line.unicode("gbk")encode("utf-8")
	print type(line)
	for x in xrange(0,len(line)):
		print line[x]
	break
fr.close()