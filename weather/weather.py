#!/usr/bin/python
#coding:utf-8 
#
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://www.weather.com.cn/textFC/hb.shtml'

def main():
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Host':'www.weather.com.cn',
	'Referer':'http://www.weather.com.cn/textFC/db.shtml',
	'Upgrade-Insecure-Requests':'1',
	'X-Anit-Forge-Token':None,
	'X-Requested-With':"XMLHttpRequest"
	}
	result = requests.get(url,headers = headers)
	content = result.content
	soup = BeautifulSoup(content,'lxml')
	conMid_list = soup.find_all('div',class_ = 'conMidtab2')
	for x in conMid_list:
		print x

if __name__ == '__main__':
	main()