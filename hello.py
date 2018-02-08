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

#os.remove('hello.txt')
#
path = os.getcwd()
test_path = os.path.join(path,'test')
all_files = os.listdir(test_path)
for file in all_files:
	file_com = os.path.splitext(file)
	file_name = file_com[0]
	extra_name = file_com[1]
	new_file = file_name + 'hellow' + extra_name
	old_file_path = os.path.join(test_path,file)
	new_file_path = os.path.join(test_path,new_file)
	os.rename(old_file_path,new_file_path)
	fp = open(new_file_path,'w')
	fp.write("hello world")
	fp.close()