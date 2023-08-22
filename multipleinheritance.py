# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:35:23 2023

@author: Students
"""

class c1:
    def summation(self,a,b):
        print(a+b)
class c2:
    def multiplication(self,a,b):
        print(a*b)
class derived(c1,c2):
    def divide(self,a,b):
        print(a/b)
d=derived()
print(isinstance(d,derived))


d.summation(5, 10)
d.multiplication(5, 10)
d.divide(10, 2)