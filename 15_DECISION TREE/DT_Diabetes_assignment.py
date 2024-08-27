# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:50:42 2024

@author: Paresh Dhamne

Business objective :

        Maximize : he primary business objective is likely to maximize the accuracy 
        of the predictive model. 

        Minimize : While maximizing accuracy is crucial, there might be business constraints related to minimizing 
        false positives and false negatives. Depending on the business context, these errors might have different costs or implications.
 
Business Contraints :  
        Compliance with relevant regulations and standards, especially in healthcare, is a critical constraint.


DATA DICTIONARY:

'Number of times pregnant': Indicates the frequency of pregnancies for an individual.
'Plasma glucose concentration': Refers to the concentration of glucose in the blood plasma.
'Diastolic blood pressure': Represents the diastolic blood pressure measurement.
'Triceps skin fold thickness': Denotes the thickness of the skin fold on the triceps.
'2-Hour serum insulin': Represents insulin levels in the blood serum measured 2 hours after glucose intake.
'Body mass index': Refers to the body mass index, calculated from an individual's weight and height.
'Diabetes pedigree function': Represents a function assessing the likelihood of diabetes based on family history.
'Age (years)': Indicates the age of an individual in years.
'Class variable': Denotes the target variable, often indicating the presence or absence of diabetes.
"""

import pandas as pd
import numpy as np
diabe=pd.read_csv("D:/SUPERVISED ALGORTIHM/DECISION TREE/Diabetes.csv")
diabe
##################
#shape of the data
diabe.shape    
 #Out[79]: (768, 9)
###############################
#size o fthe dataset
diabe.size     
 #Out[80]: 6912
###############################
#columns
diabe.columns
##############################
#columns
diabe.describe()
'''        Number of times pregnant  ...   Age (years)
count                 768.000000  ...    768.000000
mean                    3.845052  ...     33.240885
std                     3.369578  ...     11.760232
min                     0.000000  ...     21.000000
25%                     1.000000  ...     24.000000
50%                     3.000000  ...     29.000000
75%                     6.000000  ...     41.000000
max                    17.000000  ...     81.000000 '''

#######################################
# checking te null value
a=diabe.isnull()
a.sum()
########################################
diabe.dtypes
''' Number of times pregnant          int64
 Plasma glucose concentration      int64
 Diastolic blood pressure          int64
 Triceps skin fold thickness       int64
 2-Hour serum insulin              int64
 Body mass index                 float64
 Diabetes pedigree function      float64
 Age (years)                       int64
 Class variable                   object'''
#####################################
#now we Want to rename the column name 
diabe.columns = diabe.columns.str.replace(' ', '_')
diabe
##################################################

# now let us convert th class varible column into the  numerical form
from sklearn.preprocessing import LabelEncoder
le_class=LabelEncoder()

# we are rename the column which is made with the numerical value
diabe['Outcome']= le_class.fit_transform(diabe['_Class_variable'])
diabe=diabe.drop(['_Class_variable'], axis='columns' )
X=diabe.drop('Outcome', axis='columns')
y =diabe.Outcome
############################################
#now split the dataset into the test and train dataset form

from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test= train_test_split(X,y,test_size=0.2)
################################################
#now we can apply the decision tree on the dataset
from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

#now let us a 
model.predict([[6,148,72,35,0,33.6,0.627,50]])

model.predict([[1,85,66,29,0,26.6,0.351,31]])
