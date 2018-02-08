#!/usr/bin/python
#coding:utf-8 
#

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import operator
import json
import re


###########################################################取得下发值
dic_page = []
match_down = re.findall(r'\[\d{5,}\].{30,32}server down.*?\}.*?\}',open('leshilog.txt','r').read(),re.S|re.M|re.I)
fp = open('down_cmd.txt','w+')
if match_down:
	for i in match_down:
		match_json = re.search(r'\{.*?\}.*?\}',i.replace('\n',''),re.M|re.I)
		if match_json:
			dic_page.append(match_json.group())
		else :
			print 'there is empty match_down'
		#print dic_page
#dic_txt = json.dumps(dic_page,ensure_ascii=False)
for i in dic_page:
	fp.write(i.encode('utf-8'))
	fp.write('\n')
fp.close

print '*'*40		#华丽的分割线
###########################################################取得上传值
dic_page = []
fp = open('post_state.txt','w+')
match_obj = re.findall(r'\[\d{5,}\].{30,32}data send to server.*?len=\w+',open('leshilog.txt','r').read(),re.S|re.M|re.I)
if match_obj:
	for i in match_obj:
		match_json = re.search(r'\{.*\}\]\}',i.replace('\n',''),re.M|re.I)
		if(match_json):
			dic_page.append(match_json.group())
		else:
			print "there is empty match_post"
for i in dic_page:
	fp.write(i.encode('utf-8'))
	fp.write('\n')
fp.close()


print '*'*40		#华丽的分割线
#################################################取得设备报上来的串口数据
dic_page = []
fp = open('device_report.txt','w+')
match_list = re.findall(r'\[\d{5,}\].{37,38}device.{1}.{96}',open('leshilog.txt','r').read(),re.S|re.M|re.I)
if match_list:
	for n in match_list:
		match_json = re.search(r'AA\sAA.*',n.replace('\n',''),re.M|re.I)
		if match_json:
			dic_page.append(match_json.group())
		else:
			print "there is empty match_device_report"
for i in dic_page:
	fp.write(i.encode('utf-8'))
	fp.write('\n')
fp.close()

