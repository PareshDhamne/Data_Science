# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:35:53 2024

@author: Paresh Dhamne
1.	Business Problem
1.1.	What is the business objective?
    1.1.1.Maximize:The overall salary of the employee based on its education and number of hours
                he/she is working and the capitalgain
    1.1.2.Minimize:The capitalloss of the company should be minimize as it will affect on the salary
                of the employee as well as the its performance
1.2.	Are there any constraints?
           The overall data of employee and maintaining all the information 
                               which will directly affect on the salary should be maintain


DATA DICTIONARY:
age : age of a person  is quantitative(Numeric data)       

workclass: A work class is a grouping of work is Nominal(categorical data) 

education: Education of an individuals is Nominal(categorical data)

maritalstatus: Marital status of an individulas is Nominal(categorical data)

occupation: occupation of an individuals is Nominal(categorical data)

relationship: Describes the relationship status, with categories like Wife, Own-child, Husband is Nominal(categorical data)

race: Race of an Individual is Nominal(categorical data)

sex : Gender of an Individual is Nominal(categorical data)

capitalgain: profit received from the sale of an investment is quantitative(Numeric data)

capitalloss: A decrease in the value of a capital asset is quantitative(Numeric data)

hoursperweek: number of hours work per week is quantitative(Numeric data)

native: Native of an individual is Nominal(categorical data)

Salary: salary of an individual is Nominal(categorical data)

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

salary_train_data=pd.read_csv("D:/SUPERVISED ALGORTIHM/NAVIE BAYES/SalaryData_Train.csv",encoding="ISO-8859-1")


#4.	Exploratory Data Analysis (EDA):
    
salary_train_data.columns
'''
Index(['age', 'workclass', 'education', 'educationno', 'maritalstatus',
       'occupation', 'relationship', 'race', 'sex', 'capitalgain',
       'capitalloss', 'hoursperweek', 'native', 'Salary'],
      dtype='object')
'''
###############################

salary_train_data
#[30161 rows x 14 columns]

###############################

salary_train_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30161 entries, 0 to 30160
Data columns (total 14 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   age            30161 non-null  int64 
 1   workclass      30161 non-null  object
 2   education      30161 non-null  object
 3   educationno    30161 non-null  int64 
 4   maritalstatus  30161 non-null  object
 5   occupation     30161 non-null  object
 6   relationship   30161 non-null  object
 7   race           30161 non-null  object
 8   sex            30161 non-null  object
 9   capitalgain    30161 non-null  int64 
 10  capitalloss    30161 non-null  int64 
 11  hoursperweek   30161 non-null  int64 
 12  native         30161 non-null  object
 13  Salary         30161 non-null  object
dtypes: int64(5), object(9)
memory usage: 3.2+ MB
'''
###################################
salary_train_data.dtypes
'''
age               int64
workclass        object
education        object
educationno       int64
maritalstatus    object
occupation       object
relationship     object
race             object
sex              object
capitalgain       int64
capitalloss       int64
hoursperweek      int64
native           object
Salary           object
dtype: object
'''
################################
salary_train_data.isnull().sum()
'''
#there is no null values in dataset
age              0
workclass        0
education        0
educationno      0
maritalstatus    0
occupation       0
relationship     0
race             0
sex              0
capitalgain      0
capitalloss      0
hoursperweek     0
native           0
Salary           0
dtype: int64
'''
##############################
a=salary_train_data.describe()
#it will provide 5 number summary of dataset
# The mean and meadian of the the capitalgain and capitaloss showing measure diffrence 
# so to minimize it we have to normalize it
#############################

#Visualize the data
sns.boxplot(salary_train_data)
#capitalgain has outlier
#so normalize data

#####################################
# Normalization of the data

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(a)
df_norm
'''
   age  educationno  capitalgain  capitalloss  hoursperweek
count  1.000000     1.000000     0.301613     1.000000      1.000000
mean   0.000839     0.000302     0.010921     0.002928      0.001324
std    0.000000     0.000051     0.074065     0.013399      0.000364
min    0.000128     0.000000     0.000000     0.000000      0.000000
25%    0.000493     0.000265     0.000000     0.000000      0.001293
50%    0.000792     0.000298     0.000000     0.000000      0.001293
75%    0.001123     0.000398     0.000000     0.000000      0.001459
max    0.002550     0.000497     1.000000     0.144425      0.003249
'''

###########################################

# Read the train Data and Test data 
salary_test_data=pd.read_csv("D:/SUPERVISED ALGORTIHM/NAVIE BAYES/SalaryData_Test.csv",encoding="ISO-8859-1")
salary_test_data.head()

######################################
X=salary_test_data[['educationno','hoursperweek']]
y=salary_test_data[['Salary']]
###########################################
salary_train_data=pd.read_csv("D:/SUPERVISED ALGORTIHM/NAVIE BAYES/SalaryData_Train.csv",encoding="ISO-8859-1")
salary_train_data
############################################
x1=salary_train_data[['educationno','hoursperweek']]
y1=salary_train_data[['Salary']]

from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb=MB()

# The fit the model
classifier_mb.fit(x1,y1)
####################################
# Check the accuracy of the model

y_pred = classifier_mb.predict(X)  
y_pred

from sklearn.metrics import accuracy_score

# Assuming y_pred is the predicted values and y is the actual values
accuracy = accuracy_score(y, y_pred)
accuracy
################################################################

