# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:12:21 2023

@author: Students
"""

class A:
    def __init__(self,a):
        self.a=a
        
    def __add__(self,other):
        return self.a+other.a 
ob1=A(1)
ob2=A(2)
print(ob1+ob2)

ob3=A("Geeks ")
ob4=A("For")
print(ob3+ob4)

print(A.__add__(ob1,ob2))