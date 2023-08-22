# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:57:40 2023

@author: Students
"""

class A:
    def __init__(self,a):
        self.a=a
        
    def __add__(self,other):
        return self.a+other.a
    
    def __ge__(self,m):
        if self.a<=m.a:
            print(m.a, " is greater")
            
obj1=A(10)
obj2=A(20)

print(obj1+obj2)
b=obj1.__add__(obj2)
print(b)

obj1.__ge__(obj2)