# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:37:00 2024

@author: Paresh Dhamne

Business Objective:

        Maximize : The Correct classification of the dataset information wheher the person having tumor 
        or not by classifying and checking the parameters values

        Minimize : The false prediction of the data i.e the tumor prediction so the correct prescription 
        should be taken from the patient side

Business Contraints : 
    The information regarding the tumor should be secure so the mishandling of the data will be less.

#Data Dictionary
id: An identifier for each entry (non-null integer).
diagnosis: A categorical variable indicating the diagnosis (non-null object).
radius_mean: Mean of distances from center to points on the perimeter (non-null float).
texture_mean: Standard deviation of gray-scale values (non-null float).
perimeter_mean: Mean size of the core tumor (non-null float).
area_mean: Mean size of the core tumor (non-null float).
smoothness_mean: Mean of local variation in radius lengths (non-null float).
compactness_mean: Mean of perimeter^2 / area - 1.0 (non-null float).
concavity_mean: Mean of severity of concave portions of the contour (non-null float).
points_mean: Mean for number of concave portions of the contour (non-null float).
symmetry_mean: Mean symmetry (non-null float).
dimension_mean: Mean of fractal dimension (non-null float).
radius_se: Standard error for the mean of distances from center to points on the perimeter (non-null float).
texture_se: Standard error for the standard deviation of gray-scale values (non-null float).
perimeter_se: Standard error for the mean size of the core tumor (non-null float).
area_se: Standard error for the mean size of the core tumor (non-null float).
smoothness_se: Standard error for local variation in radius lengths (non-null float).
compactness_se: Standard error for perimeter^2 / area - 1.0 (non-null float).
concavity_se: Standard error for severity of concave portions of the contour (non-null float).
points_se: Standard error for number of concave portions of the contour (non-null float).
symmetry_se: Standard error for symmetry (non-null float).
dimension_se: Standard error for fractal dimension (non-null float).
radius_worst: Worst (largest) mean value for mean of distances from center to points on the perimeter (non-null float).
texture_worst: Worst (largest) mean value for standard deviation of gray-scale values (non-null float).
perimeter_worst: Worst (largest) mean value for the mean size of the core tumor (non-null float).
area_worst: Worst (largest) mean value for the mean size of the core tumor (non-null float).
smoothness_worst: Worst (largest) mean value for local variation in radius lengths (non-null float).
compactness_worst: Worst (largest) mean value for perimeter^2 / area - 1.0 (non-null float).
concavity_worst: Worst (largest) mean value for severity of concave portions of the contour (non-null float).
points_worst: Worst (largest) mean value for number of concave portions of the contour (non-null float).
symmetry_worst: Worst (largest) mean value for symmetry (non-null float).
dimension_worst: Worst (largest) mean value for fractal dimension (non-null float).


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

data=pd.read_csv("D:/SUPERVISED ALGORTIHM/ADABOOST/Tumor_Ensemble.csv")

#Data information
data.head()
data.info()
data.isna().sum()
#There is no null value present in given dataset

#EDA
target=data["diagnosis"]
sns.countplot(x=target,palette='winter')
plt.xlabel("diagnosis")
#our data is evenly distributed. Atleast 200 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#observations

#1) radius_mean ,texture_mean ,perimeter_mean  and area_mean,points_mean,radius_se are highly correlated to each other

sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of tumor patient based on area_mean and area_worst',fontsize=20)

ax1=sns.histplot(x='area_mean',data=data,hue='diagnosis',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='area_mean',title='Distribution of Dtumor patient based on diagnosis')

ax2=sns.histplot(x='area_worst',data=data,hue='diagnosis',kde=True,ax=ax[1],palette='coolwarm')
ax2.set(xlabel='area_worst',title='Distribution of tumor patient based on diagnosis')

plt.show()

data.hist(bins=30,figsize=(20,15),color='#005b96');

#As we cans ee there are outliers in radius_mean, _texture_mean,concavity_mean,dimension_mean,texture_se

sns.boxplot(x=data["radius_mean"])
sns.boxplot(x=data["texture_mean"])
sns.boxplot(x=data["concavity_mean"])
sns.boxplot(x=data["dimension_mean"])
sns.boxplot(x=data["texture_se"])

#checking skewness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df

#area_se column is clearly skewed as we also saw in the histogram

for column in skew_df.query("Skewed==True")['Feature'].values:data[column]=np.log1p(data[column])

data.head()
#Encoding
data1=data.copy()
data1=pd.get_dummies(data1)
data1.head()
#Scaling
data2 = data1.copy()
sc=StandardScaler()
data2[data1.select_dtypes(np.number).columns]=sc.fit_transform(data2[data1.select_dtypes(np.number).columns])
data2.drop(['diagnosis_B'],axis=1,inplace=True)
data2.head()

from sklearn.preprocessing import LabelEncoder
le__Class_variable=LabelEncoder()

data['diagnosis']= le__Class_variable.fit_transform(data['diagnosis'])
data

#Splitting
data_f=data2.copy()
target=data['diagnosis']
target=target.astype(int)
target

X_train,X_test,y_train,y_test=train_test_split(data_f,target,test_size=0.2,stratify=target,random_state=42)

#Modeling
from sklearn.ensemble import  AdaBoostClassifier

ad_clf=AdaBoostClassifier(learning_rate=0.02,n_estimators=5000)
ad_clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#Evaluation on testing data
confusion_matrix(y_test, ad_clf.predict(X_test))
accuracy_score(y_test, ad_clf.predict(X_test))

#Evalution on Training data
accuracy_score(y_train,ad_clf.predict(X_train))
