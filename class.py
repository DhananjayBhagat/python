# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:15:26 2023

@author: Students
"""

class library:
    name=input("Enter the name")
    roll=int(input("Enter the Roll no"))
    
    def _init_(self,name,roll):
        self.lname=name
        self.lroll=roll
        
    def printname(self):
        print(self.name,self.roll)
        
class student(library):
    def _init_(self,name,roll):
        library_init_ (self,name,roll)

x=student()
x.printname()