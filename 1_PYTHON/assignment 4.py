# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:47:24 2023

@author: Hp
"""

def leap_year(year):
    if(year%100==0):
        if(year%400==0):
           return True
    elif(year%4==0):
        return True
    return False
print(leap_year(2021))


#generate a random password
#when while defining any function first letter is small and next word letter is large
#then it is camel naming method

from random import randint
SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

def randomPassword():
    randomLength = randint(SHORTEST,LONGEST)
    
    result=" "
    for i in range(randomLength):
        randomChar=chr(randint(MIN_ASCII,MAX_ASCII))
    #THE CHAR FUNCTION TAKES AN ASCII COSE AS ITS
    #PARAMETER AND CNVERT IT INTO THE STRING.
        result=result+randomChar
    return result
print("Your random password is:",randomPassword())



#write a python code to find fib series  
def fibo(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    elif (n>1):
        return(fibo(n-1)+fibo(n-2))
num = int(input("Enter the number:"))
for n in range(num):
    print(fibo(n),end=" ")
print(fibo(num))
        