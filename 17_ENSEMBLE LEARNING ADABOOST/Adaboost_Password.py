# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:20:25 2024

@author: PARESH DHAMNE

Business Objective :

        Maximize : The Strength of the password we have to maximize as possible as so
        the hacker cannot crack or identify the pattern of the password

        Minimize : The weak password count 

Business Contraints : 
    The password security should be maintain so the users or client should trust on us.

#DATA DICTIONARY
characters: This column contains objects (presumably strings) 
characters_strength: This column contains integer values 
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

data=pd.read_excel("D:/SUPERVISED ALGORTIHM/ADABOOST/Ensemble_Password_Strength.xlsx")

#Data information
data.head()
data.info()
data.isna().sum()

#EDA
target=data["characters_strength"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Password Strength")
#our data is oddly distributed. Atleast 250 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')
'''
from sklearn.preprocessing import LabelEncoder
le_characters=LabelEncoder()

data['characters'] = data['characters'].astype(str)
data['characters']= le_characters.fit_transform(data['characters'])
data
'''
sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(1,figsize=(20,13))

plt.suptitle('Distribution of characters based on characters_strength',fontsize=20)

ax1=sns.histplot(x='characters',data=data,hue='characters_strength',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='characters',title='Distribution of characters based on characters_strength')


plt.show()

data.hist(bins=30,figsize=(20,15),color='#005b96');

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df

#characters_strength column is clearly skewed as we also saw in the histogram

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
data2.drop(['characters_strength'],axis=1,inplace=True)
data2.head()

#Splitting
data_f=data2.copy()
target=data['characters_strength']
target=target.astype(int)
target

X_train,X_test,y_train,y_test=train_test_split(data_f,target,test_size=0.2,stratify=target,random_state=42)

#Modeling
from sklearn.ensemble import  AdaBoostClassifier

ad_clf=AdaBoostClassifier(learning_rate=0.02,n_estimators=100)
ad_clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#Evaluation on testing data
confusion_matrix(y_test, ad_clf.predict(X_test))
accuracy_score(y_test, ad_clf.predict(X_test))

#Evalution on Training data
accuracy_score(y_train,ad_clf.predict(X_train))


