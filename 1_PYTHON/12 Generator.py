# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:34:46 2023

@author: Hp
"""

#GENERATOR
#it is another way of creating iterators
#it uses keyword 'yield'
#it is used witout function define
#in generator we get object
gen=(x
    for x in range(3)
    )
print(gen)
for i in gen:
    print(i)
    
#if we want to generate only single output then we used next method it will 
#show only first value and for second value we have to again insert next(gen)
gen=(x
    for x in range(3)
    )
next(gen)
next(gen)

#function which return multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
    
#now insted of using for loop
def range_even(end):
    for num in range(0,end,2):
        yield num
gen=range_even(6)
next(gen)
next(gen)

#chaning generator
def lengths(x):
    for ele in x:
        yield len(ele)
        
def hide(x):
    for ele in x:
        yield ele*'*'

passwords = ["not_good",'King@1234','001000=44']

for password in hide(lengths(passwords)):
    print(password)
    
#printing list with index
lst=["milk",'Egg',"Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
    
for index, item in enumerate(lst,start=1):
    print(f"{index}{item}")
    
#Use zip function
name=['dada','mama','kaka']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

#use of zip function with mis match list
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)
    
#zip_longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

#use of fill value inseted none
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
#use of all(), if all the values are true then
lst = [2,3,6,8,9]
if all(lst):
    print("All values are true")
else:
    print("Useless")
    
lst = [2,3,6,0,8,9]
if all(lst):
    print("All values are true")
else:
    print("Useless")
    
#use of any
lst =[0,0,0,8,0]
if any(lst):
    print("It has some value")
else:
    print("Useless")
    
lst =[0,0,0,0,0]
if any(lst):
    print("It has some value")
else:
    print("Useless")
    
#count
from itertools import count
counter = count()
print(next(counter))
print(next(counter))
print(next(counter))

#now let us start from 1
from itertools import count
counter = count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#cycle()
#suppose you have repeated tasks to be done
import itertools
instructions =("Eat","code",'sleep')
for instruction in itertools.cycle(instructions):
    print(instruction)
    
#repeat
from itertools import repeat
for msg in repeat("Keep PAtience",times=3):
    print(msg)
    
#combinations()
from itertools import combinations
players = ['john','jani','janardhan']
for i in combinations(players,2):
    print(i)
    

    


