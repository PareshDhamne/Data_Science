# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:16:49 2023

@author: Hp
"""

#Decorators
#pre-requisite to decorators
def plus_one(number):
    number1=number+1
    return number1
plus_one(5)
###############################

#defining function inside function
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(5)
#################################
#passing functon as arguments to other functions
def plus_one(number):
    result1=number + 1 
    return result1

def function_call(function):
    result=function(5)
    return result
function_call(plus_one)
##################################
#function returning other function
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi 
hello=hello_function()
hello()
'''
always remember when you call hello_function()
directly then it will display object not hi
therefore you need to assign it to hello firt
then call hello() function
'''
#################################

#a python decorator is a function
#that takes in a funcition and
#returns it by adding some functionality.
def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper 
decorate=uppercase_decorator(say_hi)
decorate()
#however python provides a much easier way
#for us to apply decorratiors
#we simply use the @symbol before
#the function we'd like to decorte.
##############################
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()
###############################
#applying multiple decorators
#to a single function
#we can use multiple decorators
#to a single function. However,
#the decorators will be applied in the order
#that we've called them.
def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper 
@split_string 
@uppercase_decorator 
def say_hi():
    return 'Hello There'
say_hi()
##################################
numbers=[2,6,7,8]
def cal_square(numbers):
    result=[]
    for i in numbers:
        result.append(i*i)
    return result

def cal_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i)
    return result
print(cal_square(numbers))
print(cal_cube(numbers))
##############################
import time
def cal_square(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i)
    
    end=time.time()
    print((end-start)*1000)
    print(" took " + str((end-start)*1000) + "mil sec")
    return result

def cal_cube(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i*i)
    
    end=time.time()
    print((end-start)*1000)
    print(" took " + str((end-start)*1000) + "mil sec")
    return result

array = range(1,100000)
out_square = cal_square(array)
out_cube = cal_cube(array)
#####################################

import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end=time.time()
        print(func.__name__+" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper 

@time_it 
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result
@time_it 
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)