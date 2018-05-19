#!/usr/bin/python
#coding:utf-8
#

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re

myfile=open('fog_id.txt','rb')
image_file=myfile.read()
li=image_file.split(',')
out_file = li[0]+'0'*56+li[1]+'0'*80
print out_file
outfile=open('out.bin','wb')
outfile.write(out_file)
outfile.close()
myfile.close()
print "fog id write bin success!"