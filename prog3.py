# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:58:12 2020

@author: SWPRASA
"""

a = [1,1,2,3,5,8,13,21,34,55,89]

print([i for i in a if i<5])
#-------------------

b=[]

for i in a:
    if i<5:
       b.append(i)
print(b)

#----------------------
num = int(input("Enter number: "))
newnum = []

for i in a:
    if i<num:
        newnum.append(i)
        
print(newnum)


newnum2=print([i for i in a if i<num])