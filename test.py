#coding:utf-8
import operator


x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]  
sorted_x = sorted(x, key=operator.itemgetter('name'),reverse = True)  
print sorted_x  