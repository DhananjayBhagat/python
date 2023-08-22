# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:09:57 2023

@author: Students
"""

class food_delivery:
    distance=int(input("\nEnter the Distance for zomato foood delivery : "))
    order=500
    
    if(distance==2):
        charges=20+order
        print("The Charges of Food Delivery is : ",charges)
    elif(distance>2 and distance<=4):
        charges=50+order
        print("The Charges of Food Delivery is : ",charges)
    elif(distance>4 and distance<=7):
        charges=70+order
        print("The Charges of Food Delivery is : ",charges)
    elif(distance>7):
        charges=order+70+(distance*5)
        print("The Charges of Food Delivery is : ",charges)
        
zomato=food_delivery()