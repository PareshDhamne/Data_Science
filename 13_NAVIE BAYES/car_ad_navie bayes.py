# -*- coding: utf-8 -*-
'''
Created on Mon Jan 29 23:08:29 2024

@author: Paresh Dhamne


1.	Business Problem
1.1.	What is the business objective?
    1.1.1.Maximize:Mximize the overall engegement and promotion of product by business clients on social network to increse the purhchase of this luxury SUV.
    1.1.2.Minimize:Minimize the false information and negative feddback from clients.
1.2.	Are there any constraints?
           Ensure that the use of the social network data complies with privacy regulations and ethical considerations.
           

DATA DICTIONARY:
    
User ID: Unique id for each user quantitative data(numrical data)
Gender: shows gender of client is nominal data(categorical data)
Age: Shows age of client is quantitative(Numeric data)
EstimatedSalary: shows the sallary of the client is quantitative data(numrical data)
purchased: shows the car is purchase or not is nominal data(categorical data)
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

suv_data=pd.read_csv("D:/SUPERVISED ALGORTIHM/NAVIE BAYES/NB_Car_Ad.csv",encoding="ISO-8859-1")


#4.	Exploratory Data Analysis (EDA):
    
suv_data.columns
'''
Index(['User ID', 'Gender', 'Age', 'EstimatedSalary', 'Purchased'], dtype='object')
'''
###############################

suv_data
#[400 rows x 5 columns]]

###############################

suv_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 400 entries, 0 to 399
Data columns (total 5 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   User ID          400 non-null    int64 
 1   Gender           400 non-null    object
 2   Age              400 non-null    int64 
 3   EstimatedSalary  400 non-null    int64 
 4   Purchased        400 non-null    int64 
dtypes: int64(4), object(1)
memory usage: 15.8+ KB
'''
###################################
suv_data.dtypes
'''
User ID             int64
Gender             object
Age                 int64
EstimatedSalary     int64
Purchased           int64
dtype: object
'''
################################
suv_data.isnull().sum()
'''
#there is no null values in dataset
User ID            0
Gender             0
Age                0
EstimatedSalary    0
Purchased          0
dtype: int64
'''
##############################
a=suv_data.describe()
a
#it will provide 5 number summary of dataset
# The mean and meadian of the the capitalgain and capitaloss showing measure diffrence 
# so to minimize it we have to normalize it
#############################

#Visualize the data
sns.boxplot(suv_data)
#no outlier
############################################

x=suv_data[['EstimatedSalary']]
y=suv_data[['Purchased']]

from sklearn.naive_bayes import GaussianNB as GB
classifier_mb=GB()

# The fit the model
classifier_mb.fit(x,y)
####################################
# Check the accuracy of the model

y_pred = classifier_mb.predict(x)  
y_pred

from sklearn.metrics import accuracy_score

# Assuming y_pred is the predicted values and y is the actual values
accuracy = accuracy_score(y, y_pred)
accuracy
#0.6425