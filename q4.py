# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:09:49 2026

@author: adity
"""

hours = int(input("enter hours: "))
minutes = int(input("enter minutes: "))
minutes = minutes + 15

if minutes >= 60:
    minutes = minutes - 60
    hours = hours + 1
if hours == 24:
    hours = 00
    
print(hours,":",minutes)
    
    