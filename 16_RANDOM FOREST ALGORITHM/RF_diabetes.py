# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:22:16 2024

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
df=pd.read_csv("D:/SUPERVISED ALGORTIHM/RANDOM FOREST ALGORITHM/Diabetes.csv")


#now we Want to rename the column name 
df.columns = df.columns.str.replace(' ', '_')
df.columns
##########################

df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column                         Non-Null Count  Dtype  
---  ------                         --------------  -----  
 0   _Number_of_times_pregnant      768 non-null    int64  
 1   _Plasma_glucose_concentration  768 non-null    int64  
 2   _Diastolic_blood_pressure      768 non-null    int64  
 3   _Triceps_skin_fold_thickness   768 non-null    int64  
 4   _2-Hour_serum_insulin          768 non-null    int64  
 5   _Body_mass_index               768 non-null    float64
 6   _Diabetes_pedigree_function    768 non-null    float64
 7   _Age_(years)                   768 non-null    int64  
 8   _Class_variable                768 non-null    object 
dtypes: float64(2), int64(6), object(1)
memory usage: 54.1+ KB
'''
###########################

df.isnull().sum()
'''
_Number_of_times_pregnant        0
_Plasma_glucose_concentration    0
_Diastolic_blood_pressure        0
_Triceps_skin_fold_thickness     0
_2-Hour_serum_insulin            0
_Body_mass_index                 0
_Diabetes_pedigree_function      0
_Age_(years)                     0
_Class_variable                  0
dtype: int64
'''
################################

df.shape
#Out[120]: (768, 9)

df.columns
'''
Index(['_Number_of_times_pregnant', '_Plasma_glucose_concentration',
       '_Diastolic_blood_pressure', '_Triceps_skin_fold_thickness',
       '_2-Hour_serum_insulin', '_Body_mass_index',
       '_Diabetes_pedigree_function', '_Age_(years)', '_Class_variable'],
      dtype='object')
'''
#############################

df.describe()
#there is difference between mean and median
##############################

from sklearn.preprocessing import LabelEncoder
le__Class_variable=LabelEncoder()

df['_Class_variable']= le__Class_variable.fit_transform(df['_Class_variable'])
df

X=df.drop("_Class_variable",axis=1)
y=df._Class_variable


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