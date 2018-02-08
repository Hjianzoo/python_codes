#!/usr/bin/python
#coding:utf-8 


from Tkinter import *
root = Tk()
root.title('hello world')
root.geometry('300x200')
l = Label(root,text = '校训'.decode('gbk').encode('utf-8'),bg = 'blue',font = \
    ('Arial',20)).pack()

frm = Frame(root)
frm_L = Fram(frm)
Label(frm_l,txt = '厚德'.decode('gbk').encode('utf8'),font = ('Arial',15)).pack(side = TOP)
Label(frm_l,txt = '博学'.decode('gbk').encode('utf8'),font = ('Arial',15)).pack(side = TOP)
frm.pack(side = LEFT)
frm_R = Frame(frm)
Label(frm_R,txt = '敬业'.decode('gbk').encode('utf8'),font = ('Arial',15)).pack(side = TOP)
Label(frm_R,txt = '乐群'.decode('gbk').encode('utf8'),font = ('Arial',15)).pack(side = TOP)
frm.pack(side = RIGHT)
frm.pack()
root.mainloop()