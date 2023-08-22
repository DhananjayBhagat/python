# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:29:07 2023

@author: Students
"""

class DYPatiluniversity:
    name=input("\nEnter the Name of Student : ")
    branch=input("\n Enter the Name of Branch : ")
    score_percentage=int(input("\n Enter the Score Percentage : "))
    
    fees=150000
    
    if(branch=="Arts" and score_percentage>=90):
        scholarship=(fees)/2
        print("scholarship is :",scholarship)
    elif(branch=="Engineering" and score_percentage>=85):
        scholarship=(fees)/2
        print("scholarship is :",scholarship)
    elif(branch=="Engineering" and score_percentage%7==0):
        scholarship=(fees)/20
        print("scholarship is :",scholarship)
    elif(branch=="BSC-IT" and (score_percentage%2)!=0):
        scholarship=(fees)/14.
        
        print("scholarship is :",scholarship)
        
        
degree=DYPatiluniversity()
        
    
        