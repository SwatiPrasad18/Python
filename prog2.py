# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:52:08 2020

@author: SWPRASA
"""

##Depending on whether the number is even or odd, print out an appropriate message to the user.
try:
    number = int(input("Enter number: "))
    check = int(input("Enter:"))

    if(number%4 == 0):
        print("Four")
    elif(number%2 == 0):
        print("Even")
    else:
        print("Odd")
        
    if(number%check == 0):
        print("Evenly divides")
    else:
        print("not even")
except ValueError:
    print("Check value")