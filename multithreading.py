# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:04:31 2023

@author: Students
"""
import threading
import _thread
import time

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)
        
ob=A(11,77)
ob1=A(33,25)
t1=threading.Thread(target=ob.add)
t2=threading.Thread(target=ob.sub)

t1.start()
time.sleep(5)

t2.start()
time.sleep(2)

_thread.start_new_thread(ob.add,())
time.sleep(5)
_thread.start_new_thread(ob1.sub,())
time.sleep(6)