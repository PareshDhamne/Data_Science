# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 08:11:42 2023

@author: Hp
"""

#functions
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "The number is not prime"
            break
    return "Number is prime"
print(prime_num(2))

#without passing argumnts
def greet():
    print("Hello!")
    
def greet_n(username):
    print(f"Hello,{username}!")
greet_n("Paresh")

#argumnets and parameters
def describe(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name}")
describe('Dog','Sam')
#order matters in positional argumnets

#default values
#when eriting function, you can define a default
def describe(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name}")
describe(pet_name='Moti')

#return values
def get_formatted_data(first_name,last_name):
    #return afull name in neatly format.
    full_name = f"{first_name}{last_name}"
    return full_name
musician = get_formatted_data('Ram',' Sarkar')
print(musician) 
    
#returning a dictionary in function
def build_person(first_name,last_name):
    person={'first_name':first_name,'last_name':last_name}
    return person
musician = build_person('Ram','Shankar')
print(musician)

#passing a list
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
usernames = ['Ram',"Sam","bhim"]
greet_users(usernames)

#passing an arbitary number of argumnets
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','panner','ggreen papers','extra cheese')

def make_pizza(*toppings):
    print("\nMaking a pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','panner','ggreen papers','extra cheese')

#mixing positional and arbitary argumnets
def make_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','panner','ggreen papers','extra cheese')

#import is used to get another py file to get output
#here pizza.py is another file and we import that file
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','panner','ggreen papers','extra cheese')

#importing spcific functions
from pizza import make_pizza
make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','panner','ggreen papers','extra cheese')

#Using as to give functions as alis 
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','panner','ggreen papers','extra cheese')

#using as to give module as alias
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','panner','ggreen papers','extra cheese')

#importing all functions in a module
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','panner','ggreen papers','extra cheese')

#variable which is declare in module is local variable
#variable which is declare in function is restrcted variable
