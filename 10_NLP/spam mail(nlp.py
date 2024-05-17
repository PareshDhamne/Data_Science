# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:50:01 2023

@author: Paresh Dhamne
"""
import pandas as pd
import numpy as np

#read the csv

df=pd.read_csv("D:/Datasets/spam.csv")
#####################################
#check first 10 records
df.head()
###################################

#Total no of spam and ham
df.Category.value_counts()
####################################

#create one more column comprises of 0 and 1
#name of column is spam

df['spam']=df['Category'].apply(lambda x:1 if x=='spam' else 0)
df.shape
################################

#Train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.Message,df.spam,test_size=0.2)

#let us check the shhape of x train data and x_test data

X_train.shape
X_test.shape
#let us check the type of X-Train and X_test

type(X_train)
type(X_test)
####################################

#create bag of words representation using countVectorizer

from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
X_train_cv=v.fit_transform(X_train.values)
X_train_cv

#After creation of Bow, let us check the shape
X_train_cv.shape
###################################

#Train the naive bayes model
from sklearn.naive_bayes import MultinomialNB
#Initialize the model
model=MultinomialNB()
#Train the mdoel
model.fit(X_train_cv,y_train)
##################################

#creaye bag of words representation using Countvectorizer of x_test

X_test_cv = v.transform(X_test)
#################################

#Evalute Performance
from sklearn.metrics import classification_report
y_pred = model.predict(X_test_cv)
print(classification_report(y_test, y_pred))
