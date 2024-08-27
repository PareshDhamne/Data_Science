# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:51:48 2024

@author: Paresh Dhamne


 Business Problem:
     Maximize: For a Cloth Manufacturing company , it is an important of them to know about
    what are the factors that are responsible for high sales for their product.
     Minimize: Ensure that they can take care of these aspect and develope their product accordingly
    
1.1 what is business constaints:
    Understand the factors that are leading to high sales of the product and maintain them


DATA DICTIONARY:
Sales -- Unit sales (in thousands) at each location Competitor 
Price -- Price charged by competitor at each location 
Income -- Community income level (in thousands of dollars) 
Advertising -- Local advertising budget for company at each location (in thousands of dollars) 
Population -- Population size in region (in thousands) 
Price -- Price company charges for car seats at each site 
ShelveLoc -- A factor with levels Bad, Good and Medium indicating the quality of the shelving location for the car seats at each site 
Age -- Average age of the local population 
Education -- Education level at each location 
Urban -- A factor with levels No and Yes to indicate whether the store is in an urban or rural location 
US -- A factor with levels No and Yes to indicate whether the store is in the US or not

"""

import pandas as pd
comp=pd.read_csv("D:/SUPERVISED ALGORTIHM/RANDOM FOREST ALGORITHM/Company_Data.csv")
comp.head()

dir(comp)
comp["Sales"]=comp.Sales
comp.head()

X=comp.drop("Sales",axis=1)
y=comp.Sales

import pandas as pd

df1=comp.copy()
df1['Sales_cat'] = pd.cut(x = df1['Sales'], bins = [0,5.39,9.32,17], labels=['Low','Medium','High'], right = False)
df1.head()

from sklearn.preprocessing import LabelEncoder
le_Sales_cat=LabelEncoder()
le_ShelveLoc=LabelEncoder()
le_Urban=LabelEncoder()
le_US=LabelEncoder()
df1['']= le_Sales_cat.fit_transform(df1['Sales_cat'])
df1['ShelveLoc']= le_ShelveLoc.fit_transform(df1['ShelveLoc'])
df1['Urban']= le_Urban.fit_transform(df1['Urban'])
df1['US']= le_US.fit_transform(df1['US'])
df1

X=df1.drop("Sales_cat",axis=1)
y=df1.Sales_cat

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=20)

model.fit(X_train,y_train)

model.score(X_test,y_test)
y_predicted=model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_predicted)
cm

#matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True)
plt.xlabel('predicted')
plt.ylabel("Truth")