#!/usr/bin/python
#coding:utf-8 

''''' 
socket 给百度发送http请求 
 
连接成功后，发送http的get请求，所搜索功能 
 
'''  
import socket  
import sys  
import time  
if __name__=='__main__':  
    #创建套接字  
    try :  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    except socket.eorror,e:  
        print 'socket false:%s'%e  
    print 'socket ...'  
     
    #连接百度ip  
    try :  
        sock.connect(('220.181.111.148',80))  
    except socket.error,e:  
        print 'connect false %s'%e  
        sock.close()  
    print 'connect ...'  
     
    #发送百度首页面请求并且保持连接  
    try :  
        print 'send start...'  
        str='GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:keep-alive\r\n\r\n'  
        sock.send(str)  
    except socket.eorror,e:  
        print 'send false'  
        sock.close()  
     
    data=''  
    data = sock.recv(1024)  
    print data