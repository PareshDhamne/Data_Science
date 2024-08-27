# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:19:05 2024

@author: PARESH DHAMNE
"""

#IMPORT NECESSARY PAKAGES
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')

#read csv file
load_data=pd.read_csv("D:/SUPERVISED ALGORTIHM/ADABOOST/income.csv")
load_data.columns
load_data.head()

#let us split the data in input and output
X=load_data.iloc[:,0:6]
y=load_data.iloc[:,6]

#split thr dataset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

#create adaboost classfier

add_model=AdaBoostClassifier(n_estimators=100,learning_rate=1)
#n_estimator=number of weak learners
#learning rate, it contributes weights of weak learners,bydefault in
#train the model

model=add_model.fit(X_train,y_train)
#predict the results
y_pred=model.predict(X_test)
print("accuracy",metrics.accuracy_score(y_test,y_pred))

#let us try for another base model
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
#here base model is changed

Ada_model=AdaBoostClassifier(n_estimators=100,base_estimator=lr,learning_rate=1)
model=Ada_model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print("accuracy",metrics.accuracy_score(y_test,y_pred))
