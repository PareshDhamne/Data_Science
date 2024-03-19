# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:14:00 2023

@author: Hp
"""

#1)Write a python program to check if a list is empty
def is_empty(lst):
    if not lst:
        return True
    else:
        return False
lst=[]
if is_empty(lst):
    print("Empty list")
else:
    print("List is not empty")
    
#2)Using list comprehenion, construct a list from the squares of each element in the list
lst=[1,2,3,4]
lst1=[i**2 for i in lst]
lst1

#3)Write a python script to check whether a given key already exist in a dictionary
states={"Maharashtra":"Mumbai",
        "Gujrat":"Gandhinagar"}
print("Maharashtra" in states)

#4)First create a range from 100 to 160 with steps 10. Second, using dict comprehension, create a dictionary
#where each number in the range is the key and each item is divided by 100
dict = {
        x:x*x
        for x in range(3)
        }
print(dict)

    
#5)create a dataframe which comprises course,fees, and duration and add tutor column
import pandas as pd
df={"Courses":["Python","Java"],
    "fees":[5000,4000],
    "duration":["35 hrs","35 hrs"]}
df
df1=pd.DataFrame(df)
df1

tutors=["Ram","Sham"]
df2=df1.assign(TutorsAssigned=tutors)
df2

#6)You have already created dataframe, write it to csv
df3=df1.to_csv("Paresh.csv")
df3
#7)write a python function which returns multiple  values
def multiple(*arg):
    return arg
multiple("Ram","Sham")
#8)write a function which takes two arguments :a,b and return the multiplication of them
mult=lambda a,b:a*b
mult(4,5)

#9)write a numpy program to test if any of the elements of a given array are non_zero.
import numpy as np
array=[1,0,0,0]
print(np.any(array))

#10)Write a python to plot two or more lines and set the line markers.
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5,6])
plt.plot([5,6,7,8,9])
plt.show()
#11)Write a python programming to display a bar chart of the popularity of programming languages.
#Sample data:
    #programming languages:java,python,PHP,Javascript,C#,C++
    #popularity:22.2,23.7,8.8,8,7.7,6.7
x=["Java","Python","PHP","JavaScript","C#","C++"]
y=[22.2,23.7,8.8,8,7.7,6.7]
plt.xlabel("Prohramming languages")
plt.ylabel("popularity")
plt.bar(x,y)

