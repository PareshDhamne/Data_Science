# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:43:16 2024

@author: PARESH DHAMNE

Business Understing:
    Maximize: Improve the model's ability to accurately predict monthly income, 
    enhancing its effectiveness in identifying accurate salary claims.

    Minimize: Reduce discrepancies between claimed and predicted incomes to minimize 
    the risk of candidates providing inaccurate salary information.

        
Business constraints:
    Adhere to relevant regulations, especially those related to data 
    protection and privacy in the recruitment domain.
 

DATA DICTIONARY

Position_of_the_employee --  shows the position of the employee -- nominal data
no_of_Years_of_Experience_of_employee -- shows the experience of employee -- quantitative data
_monthly_income_of_employee -- shows the income of employee -- quantitative data

"""


import pandas as pd
df=pd.read_csv("D:/SUPERVISED ALGORTIHM/RANDOM FOREST ALGORITHM/HR_DT.csv")


#now we Want to rename the column name 
df.columns = df.columns.str.replace(' ', '_')
df.columns
##########################

df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 196 entries, 0 to 195
Data columns (total 3 columns):
 #   Column                                 Non-Null Count  Dtype  
---  ------                                 --------------  -----  
 0   Position_of_the_employee               196 non-null    object 
 1   no_of_Years_of_Experience_of_employee  196 non-null    float64
 2   _monthly_income_of_employee            196 non-null    int64  
dtypes: float64(1), int64(1), object(1)
memory usage: 4.7+ KB
'''
###########################

df.isnull().sum()
'''
Position_of_the_employee                 0
no_of_Years_of_Experience_of_employee    0
_monthly_income_of_employee              0
dtype: int64
'''
################################

df.shape
#Out[15]: (196, 3)

df.columns
'''
Index(['Position_of_the_employee', 'no_of_Years_of_Experience_of_employee',
       '_monthly_income_of_employee'],
      dtype='object')
'''
#############################

df.describe()
#there is difference between mean and median
##############################

from sklearn.preprocessing import LabelEncoder
le_Position_of_the_employee=LabelEncoder()

df['Position_of_the_employee']= le_Position_of_the_employee.fit_transform(df['Position_of_the_employee'])
df

X=df.drop("Position_of_the_employee",axis=1)
y=df.Position_of_the_employee


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