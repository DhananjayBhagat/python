# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:27:27 2023

@author: Students
"""

class Person:
    def _init_(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        
class Student(Person):
    def _init_ (self,fname,lname):
        Person_init_ (self,fname,lname)

x=Student()
x.printname("prashant")