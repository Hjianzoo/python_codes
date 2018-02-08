#!/usr/bin/python  
# -*- conding:utf-8 -*-  
  
from bottle import route, run

@route('/hello')
def hello():
    return "huang jian zhong"

run(host="localhost", port=8080, debug=True)