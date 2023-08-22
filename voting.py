# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:29:00 2023

@author: Students
"""


     
try:
    age=int(input("Enter your age"))
    if age>18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")    
except ValueError:
    print("age must be a valid number")
 
except:
    print("An Error occured")
    
finally:
    print("End to Voting... Thanks for voting")
