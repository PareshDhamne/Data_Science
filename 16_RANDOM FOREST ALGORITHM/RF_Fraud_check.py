# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:00:58 2024

@author: Paresh Dhamne

Business Objective:

        Maximize: Improve the model's ability to accurately classify individuals into taxable and non-taxable income categories.

        Minimize: Reduce the occurrences of incorrectly predicting taxable or non-taxable income, as these errors may have different implications.

Business Contraints : 
        Ensure the decision tree model remains interpretable, allowing stakeholders to understand the factors influencing taxability predictions.

        
DATA DICTIONARY:

'Undergrad': Indicates whether an individual is pursuing undergraduate studies.
'Marital.Status': Specifies the marital status of an individual.
'Taxable.Income': Represents the income subject to taxation.
'City.Population': Refers to the population size of the city where an individual resides.
'Work.Experience': Denotes the number of years an individual has been employed or has relevant work experience.
'Urban': Indicates whether an individual resides in an urban area.
"""

import pandas as pd
df=pd.read_csv("D:/SUPERVISED ALGORTIHM/RANDOM FOREST ALGORITHM/Fraud_check.csv")
df

df["Taxable_Income_n"] = pd.cut(df["Taxable.Income"], bins = [10002,30000,99620], labels = ["Risky", "Good"])
df

df.columns
'''
Out[24]: 
Index(['Undergrad', 'Marital.Status', 'Taxable.Income', 'City.Population',
       'Work.Experience', 'Urban', 'Taxable.Income_n'],
      dtype='object')
'''
###########################################
df.shape
#(600, 7)
###########################################

df.isnull().sum()
'''
Out[84]: 
Undergrad           0
Marital.Status      0
Taxable.Income      0
City.Population     0
Work.Experience     0
Urban               0
Taxable_Income_n    0
dtype: int64
'''
############################################

df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 600 entries, 0 to 599
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype   
---  ------            --------------  -----   
 0   Undergrad         600 non-null    object  
 1   Marital.Status    600 non-null    object  
 2   Taxable.Income    600 non-null    int64   
 3   City.Population   600 non-null    int64   
 4   Work.Experience   600 non-null    int64   
 5   Urban             600 non-null    object  
 6   Taxable.Income_n  600 non-null    category
dtypes: category(1), int64(3), object(3)
memory usage: 29.0+ KB
'''
##############################################

df.describe()
#there is difference between mean and median
###########################################

df.drop("Marital.Status",axis=1)
df
from sklearn.preprocessing import LabelEncoder
le_Undergrad =LabelEncoder()
le_Urban=LabelEncoder()
le_US=LabelEncoder()
le_Taxable_Income_n=LabelEncoder()
df['Undergrad']= le_Undergrad.fit_transform(df['Undergrad'])
df['Urban']= le_Urban.fit_transform(df['Urban'])
df['Taxable_Income_n']= le_Taxable_Income_n.fit_transform(df['Taxable_Income_n'])
df.head()

X=df.drop(["Taxable_Income_n","Marital.Status"],axis=1)
y=df.Taxable_Income_n


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
################################################