# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:28:19 2026

@author: adity
"""

salary = float(input("enter your salary "))
years = float(input("enter years of services "))
if 0 > salary or 0 > years:
    print("invalid")
elif years > 5:
    bonus = (salary * 5)/100
    print("net bonus amout", bonus)
else:
    print("invalid for bonus")