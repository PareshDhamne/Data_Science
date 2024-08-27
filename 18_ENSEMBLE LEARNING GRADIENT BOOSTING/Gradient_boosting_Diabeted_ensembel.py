# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:39:36 2024

@author: Paresh Dhamne

Business Objective :
    
        Maximize : The correct prediction of the diabetes and the false prediction of the .

        Minimize : The false prediction of the diabetes

Business contraints : 
        The data related to the diabetes should be maintain so that the customer shouls 
        trust on the predicted resutt

Data Dictionary
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
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from scipy.stats import skew

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

data=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/ADABOOST/Diabeted_Ensemble.csv")

#now we Want to rename the column name 
data.columns = data.columns.str.replace(' ', '_')
data.columns

#Data information
data.head()
'''
Out[63]: 
   _Number_of_times_pregnant  ...  _Class_variable
0                          6  ...              YES
1                          1  ...               NO
2                          8  ...              YES
3                          1  ...               NO
4                          0  ...              YES
'''
##############################################################################

data.info()
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
##############################################################################

data.isna().sum()
'''
Out[65]: 
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
#There is no null value present in given dataset
'''
#############################################################################

#EDA
target=data["_Class_variable"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Diabetes")
#our data is evenly distributed. Atleast 250 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#observations

#1) _Number_of_times_pregnant ,_Triceps_skin_fold_thickness ,_2-Hour_serum_insulin  and _Age_(years) are highly correlated to each other


sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of Diabetes patient based on _Class_variable',fontsize=20)

ax1=sns.histplot(x='_Diastolic_blood_pressure',data=data,hue='_Class_variable',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='_Diastolic_blood_pressure',title='Distribution of Diabetes patient based on _Class_variable')

ax2=sns.histplot(x='_Plasma_glucose_concentration',data=data,hue='_Class_variable',kde=True,ax=ax[1],palette='coolwarm')
ax2.set(xlabel='_Plasma_glucose_concentration',title='Distribution of Diabetes patient based on _Class_variable')

plt.show()

data.hist(bins=30,figsize=(20,15),color='#005b96');

#As we cans ee there are outliers in _Plasma_glucose_concentration, _2-Hour_serum_insulin,_Body_mass_index

sns.boxplot(x=data["_Plasma_glucose_concentration"])
sns.boxplot(x=data["_Diastolic_blood_pressure"])
sns.boxplot(x=data["_2-Hour_serum_insulin"])
sns.boxplot(x=data["_Body_mass_index"])


#checking skewness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df

#_Diabetes_pedigree_function column is clearly skewed as we also saw in the histogram

for column in skew_df.query("Skewed==True")['Feature'].values:data[column]=np.log1p(data[column])

#Input and output Split
predictors = data.loc[:,data.columns!="_Class_variable"]
type(predictors)

target=data["_Class_variable"]
#################################################################

#Train Test partition of the data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)

from sklearn.ensemble import GradientBoostingClassifier
boost_clf=GradientBoostingClassifier()
boost_clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

confusion_matrix(y_test,boost_clf.predict(X_test))
accuracy_score(y_test,boost_clf.predict(X_test))
#Out[39]: 0.8116883116883117
#####################################################################


#Hyperparameters
boost_clf2=GradientBoostingClassifier(learning_rate=0.02,
                                        n_estimators=1000,
                                        max_depth=1)
boost_clf2.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#Evalution on testing data
confusion_matrix(y_test,boost_clf2.predict(X_test))
accuracy_score(y_test,boost_clf2.predict(X_test))
#Out[44]: 0.7922077922077922

######################################################################
#Evalution on training data
accuracy_score(y_train,boost_clf2.predict(X_train))
#Out[45]: 0.8045602605863192