# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:30:38 2020

@author: SWPRASA
"""

##Create a program that asks the user to enter their name and their age. 
##Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
name = input("Enter name :")
age = int(input("Enter age :"))
count = int(input("Enter count: "))

nowDate = datetime.datetime.now()

currentYear = int(nowDate.year)

resultYear = currentYear+(100-age)

print("You will be 100 in: "+str(resultYear))

print("---------Again----------")

print(("You will be 100 in: "+str(resultYear)+"\n")*count)