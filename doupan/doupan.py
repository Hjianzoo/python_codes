#!/usr/bin/python
#coding:utf-8 
#
#
#
#功能：将豆瓣上的电影信息爬下来，筛选有用信息存到doupan.txt中

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import json

doupan_movies = []
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start="

def main():
	fp = open('doupan.txt','w+')
	for x in range(0,11):
		the_url = url + str(x*20)
		result = requests.get(the_url)
		json_result = result.json()
		subject_page = json_result['subjects']
		for subject in subject_page:
			dict_page = {
			'name' : subject['title'],
			'rate' : subject['rate'],
			'id' : subject['id'],
			'is_new': subject['is_new'],
			}
			#doupan_movies.append(dict_page)
			text_content = json.dumps(dict_page,ensure_ascii=False)
			fp.write(text_content.encode('utf-8')+'\n')
	
	#text_content = json.dumps(doupan_movies,ensure_ascii=False)

	#with open('doupan.json','w+') as fp:
		#fp.write(text_content.encode('utf-8'))
	fp.close()
	pass



if __name__ == '__main__':
	main()