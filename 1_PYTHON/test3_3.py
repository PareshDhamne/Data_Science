# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:10:37 2023

@author: Lenovo
"""

import pandas as pd
df=pd.read_csv('emp_data.csv')
df
####################3
df.dtypes
######################
df2=df.convert_dtypes()
df2.dtypes
#########################
df3=df.astype(str)
df3.dtypes
######################
df4=df.rename({'Salary_hike':'Salary'},axis=1)
df4
######################
cols=['Salary_hike']
df5=df[cols].astype(str)
df5.dtypes
#######################
df6=df.astype({'Salary_hike':float},errors='ignore')
#####################
df6=df.astype({'Salary_hike':float},errors='raised')
#####################
df.columns
df.columns.values
df.index
df.dtypes
####################
df['Salary_hike']
####################
df[['Salary_hike','Churn_out_rate']]
#################
df7=df.drop([1,3])
df7
####################
df8=df.drop(df.index[2:])
df8
#################
df9=df.drop(['Salary_hike'],axis=1)
df9
################
df['Salary_hike'][1]
##################
df.drop(df.columns[[1]],axis=1,inplace=True)
df
####################
import pandas as pd
import numpy as np
df.columns
df.loc[:,'Salary_hike':]
###############
import random
row_label=['r0','r1','r2','r3','r4','r5','r6','r7','r8','r9']
df9 = pd.DataFrame(df, index=row_label)
df9
##############
#different ways to access row by index
df.iloc[2]             #select 2nd row
df.iloc[1:3]            #select first three rows
df.iloc[-1:]            #select last row
df.iloc[[2,3,4]]        #select particular row
df.iloc[:0]             #empty row
df.iloc[:1]             #slect first row
df.iloc[-3:]            #select last three row
df.iloc[::2]    
####################
df9.loc['r1']
df9.loc[['r1','r2','r3']]
df9.loc['r3':]
df9.loc['r2':'r5']
###################
df.dtypes
df10=df.query('Salary_hike==1580')
df10
#################3
df11=df.query('Salary_hike!=1580')
df11
################3
tutors = [1,2,3,4,5,67,8,9,45,34]
df2 = df.assign(TutorsAssigned=tutors)
print(df2)
####################3
df2 = df.assign(Discount_in_salary=lambda x: x.Salary_hike * x.Churn_out_rate / 100)
print(df2)
#################
def add_3(x):
   return x+3
df2 = df.apply(add_3)
df2
#########################
def add_4(x):
   return x+4
df["Salary_hike"] = df["Salary_hike"].apply(add_4)
df["Salary_hike"]
##########################
# apply a lambda function to each column
df2 = df.apply(lambda x : x + 10)
df2
##############################
df['Salary_hike'] = df['Salary_hike'].map(lambda A: A/2.)
print(df)
#############################
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)
################################








