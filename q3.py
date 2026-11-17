# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:46:37 2026

@author: adity
"""

shape = input("enter shape: ")
if shape == "square":
    side = float(input("enter side: "))
    area = side * side
elif shape == "rectangle":
    length = float(input("enter length: "))
    width = float(input("enter width: "))
    area = length * width
elif shape == "circle":
    radius = float(input("enter radius: "))
    area = 3.14 * radius *radius
elif shape == "triangle":
    base =float(input("enter base: "))
    height = float(input("enter height: "))
    area = 0.5 * base * height
    
print("area=" ,area)
                         
    
                 
                 