# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:44:58 2023

@author: Hp
"""

#generating random number for lotterY
from random import randrange
MIN_NUM = 1
MAX_NUM = 49
NUM_NUMS = 6
ticket_nums = []
for i in range(NUM_NUMS):
    rand = randrange(MIN_NUM,MAX_NUM+1)
    while rand in ticket_nums:
        rand = randrange(MIN_NUM,MAX_NUM+1)
    ticket_nums.append(rand)
ticket_nums.sort()
for n in ticket_nums:
    print(n,end=" ")
    print()
    
#write a pytho code to remove outliers
values = [85,46,221,4,7,43,100,66]
retval = sorted(values)
def removeOutliers(data,num_outliers):
    retval = sorted(data)
    for i in range(num_outliers):
        retval.pop(-1)
    return retval
removeOutliers(values,2)

#write a python code that determine whether your passowrod is good or bad.
#1)it must have at least 8 charecters
#2)it must have at least one upper case letter
#one lower case letter


def is_pass(password):
    if len(password)<8:
        return False
    
    upper = False
    lower = False
    digit = False
    for p in password:
        if p>='A' and p<='Z':
            upper=True
        if p>='a' and p<='z':
            lower=True
        if p>='1' and p<='9':
            digit=True     
    if upper and lower and digit:
        print("Good")
    else:
        print("Bad")
x  = input("Enter the Password:")
print(is_pass(x))
















