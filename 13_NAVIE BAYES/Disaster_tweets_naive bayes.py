# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:38:01 2024

@author: Paresh Dhamne

1.	Business Problem
1.1.	What is the business objective?
    1.1.1.Maximize:Mximize the overall prediction of real disaster
    1.1.2.Minimize:Minimize the false information andfalse tweets
1.2.	Are there any constraints?
           Ensure that the model and its predictions adhere to ethical guidelines. Avoid biases and consider potential social or cultural sensitivities associated with disaster-related content.
           
DATA DICTIONARY:

id: id of the perticular tweet is quantitative data (numrical data)
keyword: null
loaction: null
text: perticular news is nominal data (cateogrical data) 
target: shows real and fake tweets is nominal data (categorical data)  
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tweet=pd.read_csv("D:/SUPERVISED ALGORTIHM/NAVIE BAYES/Disaster_tweets_NB.csv",encoding="ISO-8859-1")


#4.	Exploratory Data Analysis (EDA):
    
tweet.columns
'''
Index(['id', 'keyword', 'location', 'text', 'target'], dtype='object')
'''
###############################

tweet.shape
#(7613, 5)

###############################

tweet.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7613 entries, 0 to 7612
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   id        7613 non-null   int64 
 1   keyword   7552 non-null   object
 2   location  5080 non-null   object
 3   text      7613 non-null   object
 4   target    7613 non-null   int64 
dtypes: int64(2), object(3)
memory usage: 297.5+ KB
'''
###################################
tweet.dtypes
'''
id           int64
keyword     object
location    object
text        object
target       int64
dtype: object
'''
################################
tweet.isnull().sum()
'''
#keyword and location are containing  null values in dataset
id             0
keyword       61
location    2533
text           0
target         0
dtype: int64
'''
##############################
a=tweet.describe()
a
#it will provide 5 number summary of dataset
# so to minimize it we have to normalize it
##################################

#drop null columns
tweet.drop(['keyword','location'],axis=1)
###################################

#Visualize the data
sns.boxplot(tweet)
#no outlier
############################################

x=tweet[['id']]
y=tweet[['target']]

from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb=MB()

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
#0.5703402075397347