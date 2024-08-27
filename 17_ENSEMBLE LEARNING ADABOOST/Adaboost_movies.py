# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:15:43 2024

@author: PARESH DHAMNE
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

data=pd.read_csv("D:/SUPERVISED ALGORTIHM/ADABOOST/movies_classification.csv")

#Data information
data.head()
data.info()
data.isna().sum()

#EDA
target=data["Start_Tech_Oscar"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Oscar Rate")
#our data is evenly distributed. Atleast 200 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#observations

#1) Lead_ Actor_Rating , Lead_Actress_rating , Director_rating  and Producer_rating are highly correlated to each other

sns.countplot(x='Genre',data=data, hue='Start_Tech_Oscar',palette='pastel')
plt.title('O chance based on Ticket Class',fontsize=10);

##observations:
    #here are more chances of getting Oscar in Drama, Comedy and Action genre.

sns.countplot(x='3D_available',data=data,hue='Start_Tech_Oscar',palette='pastel')
plt.title('O chance based on Ticket Class',fontsize=10);

##Observations:
    #It is clear from the plot that if 3d is available the there is chance ogf winning oscar

sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of Twitter_hashtsg and collection based on target variable',fontsize=20)

ax1=sns.histplot(x='Twitter_hastags',data=data,hue='Start_Tech_Oscar',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='Twitter_hastags',title='Distribution of Twitter_hashtsg and collection based on target variable')

ax2=sns.histplot(x='Collection',data=data,hue='Start_Tech_Oscar',kde=True,ax=ax[1],palette='coolwarm')
ax2.set(xlabel='Collection',title='Distribution of Twitter_hashtsg and collection based on target variable')

plt.show()

data.hist(bins=30,figsize=(20,15),color='#005b96');

#As we cans ee there are outliers in Twitter_hastags, Marketing_expense,time_taken

sns.boxplot(x=data["Twitter_hastags"])
sns.boxplot(x=data["Marketing expense"])
sns.boxplot(x=data["Time_taken"])
sns.boxplot(x=data["Avg_age_actors"])
#write code for winsorizer
#checking skewness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df

#Total Charges column is clearly skewed as we also saw in the histogram

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
data2.drop(['Start_Tech_Oscar'],axis=1,inplace=True)
data2.head()

#Splitting
data_f=data2.copy()
target=data['Start_Tech_Oscar']
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

from sklearn.metrics import accuracy_score, confusion_matrix

##Evaluation on testing data
