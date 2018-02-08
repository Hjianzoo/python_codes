#!/usr/bin/python
#coding:utf-8 
#
#
#
#功能：将doupan.txt中的列表按照‘rate'排序，输出到sort_rate.txt中

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import operator
import json

new_list = []
def main():
	fp = open('doupan.txt','r')
	for line in fp.readlines():
		line_json = json.loads(line)  #将读出来的字符串转化为字典
		new_list.append(line_json)
	fp.close()	
	print '*'*30
	f = open('sort_rate.txt','w+')
	sort_list = sorted(new_list,key = operator.itemgetter('rate'),reverse=True) #按照列表中字典的某一个元素进行排序
	for dic_page in sort_list:
		print dic_page
		dict_txt = json.dumps(dic_page,ensure_ascii=False)  #将字典转化为字符串格式
		f.write(dict_txt.encode('utf-8')+'\n')	#将字符串格式写入目标txt文件
	f.close()
			





	



if __name__ == '__main__':
	main()





'''Python引入了with语句来自动帮我们调用close()方法：
with open('/path/to/file', 'r') as f:
    print(f.read())



python文件对象提供了三个“读”方法： read()、readline() 和 readlines()。每种方法可以接受一个变量以限制每次读取的数据量。

read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。如果文件大于可用内存，为了保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。.readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
readline() 每次只读取一行，通常比readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 readline()。
注意：这三种方法是把每行末尾的'\n'也读进来了，它并不会默认的把'\n'去掉，需要我们手动去掉。


'''