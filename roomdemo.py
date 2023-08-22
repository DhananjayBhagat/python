# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:50:18 2023

@author: Students
"""

class Room:
    length=0.0
    breadth=0.0
    
    def calculate_area(self):
        print("Area of rectangle ",self.length*self.breadth)
        
study_room=Room()

study_room.length=5
study_room.breadth=42

study_room.calculate_area()