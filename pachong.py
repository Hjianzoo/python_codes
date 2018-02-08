#!/usr/bin/python
#coding:utf-8 
#
#
import requests
import json
import time


url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
def main():
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Host':'www.lagou.com',
	'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
	'X-Anit-Forge-Code':'0',
	'X-Anit-Forge-Token':None,
	'X-Requested-With':"XMLHttpRequest"
	}

	positions = []
	for x in range(1,5):
		post_data = {
		'first':'true',
		'pn': x,
		'kd':'python'
		}
		result = requests.post(url,headers = headers,data = post_data)
		json_result =  result.json()
		print '-'*30

		positions_page = json_result['content']['positionResult']['result']
		for position in positions_page:
			position_dict = {
			'position_name':position['positionName'],
			'work_year':position['workYear'],
			'salary': position['salary'],
			'district' : position['district'],
			'company_name' : position['companyFullName'],
			}
			positions.append(position_dict)
		time.sleep(3)




	line = json.dumps(positions,ensure_ascii=False)
	with open('lagou.json','w') as fp:
		fp.write(line.encode('utf-8'))



	pass

if __name__ == '__main__':
	main()