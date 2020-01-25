# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 17:52:00 2020

@author: SWPRASA
"""

import random

a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([set(a) & set(b)])        #gives a list of set

#------------------

a = range(1, random.randint(1,30))
b = range(1, random.randint(10,40))
c=[]

for num in a:
    if num in b:
        c.append(num)

print(c)