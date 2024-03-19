# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:36:53 2023

@author: Hp
"""
#pandas are used to create dataframe
import pandas as pd

f1=pd.read_csv('D:/PARESH1_python/buzzers.csv')
print(f1)
####################################################

import os
with open('buzzers.csv') as raw_data:
    print(raw_data.read())
    
##################################################

#reading csv data as lists
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
#################################################    
#reading csv data as dictionary
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
################################################
#it is used to seprate key values in the dict
with open('buzzers.csv') as data:
    #ignore= data.readlines 
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights
##############################################
#stripping the splitting your raw data
#used to remove /n
with open('buzzers.csv') as data:
    ignore= data.readlines 
    flights={}
    for line in data:
        k,v=line.strip().split(',')
        flights[k]=v
flights
###############################################
#pre request to decorators
def plus_one(number):
    number1=number + 1 
    return number1
plus_one(5)
############################################3
#define function inside function
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(7)
#########################################
#passing functions as argumnes
#to other function
def plus_one(number):
    result1=number + 1
    return result1

def function_call(function):
    result=function(5)
    return result
function_call(plus_one)
###########################################
#functions returning other function
#when there is function in another function then we have to called one variable to declare that function.
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi 
hello=hello_function()
hello()
