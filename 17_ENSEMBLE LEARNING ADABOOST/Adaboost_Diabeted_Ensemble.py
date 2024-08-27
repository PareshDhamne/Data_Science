# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:58:12 2024

@author: PARESH DHAMNE

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
'''
Out[62]: 
Index(['_Number_of_times_pregnant', '_Plasma_glucose_concentration',
       '_Diastolic_blood_pressure', '_Triceps_skin_fold_thickness',
       '_2-Hour_serum_insulin', '_Body_mass_index',
       '_Diabetes_pedigree_function', '_Age_(years)', '_Class_variable'],
      dtype='object')
'''
##############################################################################

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
###############################################################################

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
###############################################################################

#EDA
target=data["_Class_variable"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Diabetes")
#our data is evenly distributed. Atleast 250 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#observations

#1) _Number_of_times_pregnant ,_Triceps_skin_fold_thickness ,_2-Hour_serum_insulin  and _Age_(years) are highly correlated to each other
###############################################################################

sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of Diabetes patient based on _Class_variable',fontsize=20)

ax1=sns.histplot(x='_Diastolic_blood_pressure',data=data,hue='_Class_variable',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='_Diastolic_blood_pressure',title='Distribution of Diabetes patient based on _Class_variable')

ax2=sns.histplot(x='_Plasma_glucose_concentration',data=data,hue='_Class_variable',kde=True,ax=ax[1],palette='coolwarm')
ax2.set(xlabel='_Plasma_glucose_concentration',title='Distribution of Diabetes patient based on _Class_variable')

plt.show()
###############################################################################

data.hist(bins=30,figsize=(20,15),color='#005b96');

#As we cans See there are outliers in _Plasma_glucose_concentration, _2-Hour_serum_insulin,_Body_mass_index

sns.boxplot(x=data["_Plasma_glucose_concentration"])
sns.boxplot(x=data["_Diastolic_blood_pressure"])
sns.boxplot(x=data["_2-Hour_serum_insulin"])
sns.boxplot(x=data["_Body_mass_index"])

################################################################################
#checking skewness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df
'''
Out[74]: 
                         Feature      Skew  Absolute Skew  Skewed
0      _Number_of_times_pregnant  0.899912       0.899912    True
1  _Plasma_glucose_concentration  0.173414       0.173414   False
2      _Diastolic_blood_pressure -1.840005       1.840005    True
3   _Triceps_skin_fold_thickness  0.109159       0.109159   False
4          _2-Hour_serum_insulin  2.267810       2.267810    True
5               _Body_mass_index -0.428143       0.428143   False
6    _Diabetes_pedigree_function  1.916159       1.916159    True
7                   _Age_(years)  1.127389       1.127389    True
#_Diabetes_pedigree_function column is clearly skewed as we also saw in the histogram
'''
##############################################################################

for column in skew_df.query("Skewed==True")['Feature'].values:data[column]=np.log1p(data[column])

data.head()
#Encoding
data1=data.copy()
data1=pd.get_dummies(data1)
data1.head()
'''
Out[80]: 
   _Number_of_times_pregnant  ...  _Class_variable_YES
0                   1.945910  ...                    1
1                   0.693147  ...                    0
2                   2.197225  ...                    1
3                   0.693147  ...                    0
4                   0.000000  ...                    1

[5 rows x 10 columns]
'''
###############################################################################

#Scaling
data2 = data1.copy()
sc=StandardScaler()
data2[data1.select_dtypes(np.number).columns]=sc.fit_transform(data2[data1.select_dtypes(np.number).columns])
data2.drop(['_Class_variable_YES'],axis=1,inplace=True)
data2.head()
'''
Out[85]: 
   _Number_of_times_pregnant  ...  _Class_variable_NO
0                   0.825781  ...           -1.365896
1                  -0.802604  ...            0.732120
2                   1.152449  ...           -1.365896
3                  -0.802604  ...            0.732120
4                  -1.703581  ...           -1.365896

[5 rows x 9 columns]
'''
###############################################################################

from sklearn.preprocessing import LabelEncoder
le__Class_variable=LabelEncoder()

data['_Class_variable']= le__Class_variable.fit_transform(data['_Class_variable'])
data

#Splitting
data_f=data2.copy()
target=data['_Class_variable']
target=target.astype(int)
target

X_train,X_test,y_train,y_test=train_test_split(data_f,target,test_size=0.2,stratify=target,random_state=42)
###############################################################################

#Modeling
from sklearn.ensemble import  AdaBoostClassifier

ad_clf=AdaBoostClassifier(learning_rate=0.02,n_estimators=5000)
ad_clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#Evaluation on testing data
confusion_matrix(y_test, ad_clf.predict(X_test))
'''
Out[98]: 
array([[100,   0],
       [  0,  54]], dtype=int64)
'''
###############################################################################

accuracy_score(y_test, ad_clf.predict(X_test))

###############################################################################
#Evalution on Training data
accuracy_score(y_train,ad_clf.predict(X_train))

from sklearn.metrics import accuracy_score, confusion_matrix

##Evaluation on testing data
