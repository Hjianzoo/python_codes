#!/usr/bin/python
#coding:utf-8 
#
#读文件
'''
fp = open("file.txt","r")
lines= fp.readlines()
print lines
print type(lines)
for line in lines:
	print line
fp.close	
'''
import os
#修改文件名
#os.rename('file.txt','hello.txt')		

#获取当前文件所在路径
'''
path = os.getcwd()
print path
'''

#获取指定目录中的文件和文件夹
'''
file_list = os.listdir(os.getcwd())
print file_list
'''
#删除文件

os.remove('hello.txt')
