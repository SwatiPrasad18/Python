# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 17:44:01 2020

@author: SWPRASA
"""

num = int(input("Enter number: "))

a = range(2,num+1)
divisor=[]

for i in a:
    if num%i==0:
        divisor.append(i)
print(divisor)