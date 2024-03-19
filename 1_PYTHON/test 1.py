# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:34:53 2023

@author: Hp
"""

'''
Name:- DHAMNE PARESH SUNIL
TY Comp 
'''
from fnmatch import fnmatch
import pandas as pd
import pandas as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
df=pd.read_csv('D:/PARESH1_python/Data_Science_Attendance_Sheet2.csv')
df
#Q1. Rename Your name Column
df1=df.rename(columns={'Paresh Dhamne':'Paresh_Dhamne'})
df1
##############################################################

#Q2. Convert your column into list
df2=df1['Paresh_Dhamne'].tolist()
df2

#Q.3 From the derived list,find out how for how many days,you appeared 0,1,2,3,4,5,7 sessions

#Q.4 Generate a bar graph of your attendance
sns.countplot(x='Paresh_Dhamne',data=df1)

#Q.5 Generate 5 number summary using describe() and illustrate the minimum number of sessions ,max
#number of sessions and mean number of sessions you did during the training
df3=df[:6]
df3.describe()
#Q.6 Generate box plot using seaborn for your column and write the inference
sns.boxplot(df1.Paresh_Dhamne)
#Q.7 Generate joint plot using seaborn for your column and write the inference
sns.jointplot(x='Paresh Dhamne',y='Paresh Dhamne',data=df)
#Q. 8 From complete dataframe, find out how many are regular students, how many are moderate and 
#how many are poor in attendance.

#Q.11 Open the given file in read mode
filename='D:/PARESH1_python/AI_jobs_in_2024.txt'
with open(filename) as file_object:
    data = file_object.read()
print(data)
        

#Q.12 Remove the numbers from the text    

filename='D:/PARESH1_python/AI_jobs_in_2024.txt'
with open(filename) as file_object:
    data = file_object.read()
    pat=r'[^a-zA-Z.,!?/:;\"\'\s]'
    print(re.sub(pat, '',data))
 
#Q.13 How many companies were surveyed ,extract using text processing  
with open(filename) as file_object:
    data = file_object.read()
    print(data.find(r'\d+'))

#Q.14 How many companies are willing to shift in AI domain,extract using text processing  
with open(filename) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)  
 
#Q.15 How many millions jobs are expected to create in 2024 in field of AI
with open(filename) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)
#Q.16 Convert numbers into words
import inflect 
p= inflect.engine()
with open(filename) as file_object:
    data = file_object.read()
    temp_str=data.split()
    new_string=[]
    for word in temp_str:
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)
    temp_str=' '.join(new_string)
    print(temp_str)
