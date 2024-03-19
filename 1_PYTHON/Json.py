# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 08:40:20 2023

@author: Hp
"""
#JSON JAVASCRIPT OBJECT NOTATION
#USING json.dump() and json.load()
#json file

import json
numbers = [2,3,5,7,11,14,13]
filename = 'numbers.json'
with open (filename,'w') as f:
    json.dump(numbers,f)
        
import json
username = input("What is your name?")
filename ='username.json'
with open (filename,'w') as f:
    json.dump(username,f)
print(f"we'll remember you when you come back {username}!" )

#user whose name is already stored
import json
filename = 'username.json'
with open (filename) as f:
    username = json.load(f)
print(f"Welcome back,{username}!")

#using try and except block
filename = 'username.json'
try:
    with open (filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?")
    filename ='username.json'
    with open (filename,'w') as f:
        json.dump(username,f)
        print(f"we'll remember you when you come back {username}!" )
else:
    print(f"Welcome,{username}!")
    
lst = []
for i in range(0,20):
    lst.append(i)
print(lst)

#list comprherent
lst =[i for i in range(0,20)]
print(lst)

#.capitalize function is used to capital first letter of word
names =['dada','mama','kaka']
lst = [name.capitalize() for name in names]
print(lst)

#list comprenhernsion using if else
def is_even(num):
    return num%2==0
lst=[
     num 
     for num in range(10) 
     if is_even(num)
     ]
print(lst)

#Date 18-04-2023

lst=[
     f"{x}{y}"
     for x in range(3)
     for y in range(3)
     ]
print(lst)

lst=[
     f"{x}{y}{z}"
     for x in range(3)
     for y in range(3)
     for z in range(3)
     ]
print(lst)

#set comrehension
lst={x
     for x in range(4)
     }
print(lst)

#dictionary comrehension
dict = {
        x:x*x
        for x in range(3)
        }
print(dict)


