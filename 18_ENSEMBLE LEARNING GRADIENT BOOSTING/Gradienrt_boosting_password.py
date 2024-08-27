# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 23:34:39 2024

@author: Paresh Dhamne

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

data=pd.read_excel("D:/12-SUPERVISED ALGORTIHM/GRADIENT BOOSTING/Ensemble_Password_Strength.xlsx")

#Data information
data.head()
data.info()
data.isna().sum()
#No null value

######################################################################################

#EDA
target=data["characters_strength"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Password Strength")
#our data is oddly distributed. Atleast 250 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')
######################################################################################

sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(1,figsize=(20,13))

plt.suptitle('Distribution of characters based on characters_strength',fontsize=20)

ax1=sns.histplot(x='characters',data=data,hue='characters_strength',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='characters',title='Distribution of characters based on characters_strength')

plt.show()
#######################################################################################

data.hist(bins=30,figsize=(20,15),color='#005b96');
######################################################################################

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df

#characters_strength column is clearly skewed as we also saw in the histogram

for column in skew_df.query("Skewed==True")['Feature'].values:data[column]=np.log1p(data[column])
###########################################################################################

#dummy variables
data.head()
data.info()

#n-1 dummy variables will be created for n categories

data=pd.get_dummies(data,columns=["characters"],drop_first=True)

data.head()
#####################################################################
#Input and output Split
predictors = data.loc[:,data.columns!="characters_strength"]
type(predictors)

target=data["characters_strength"]
#######################################################################
#Train Test partition of the data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)

from sklearn.ensemble import GradientBoostingClassifier
boost_clf=GradientBoostingClassifier()
boost_clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

confusion_matrix(y_test,boost_clf.predict(X_test))
'''
#array([[  0,  47],
       [  0, 353]], dtype=int64
'''
accuracy_score(y_test,boost_clf.predict(X_test))
#Out[32]: 0.8825
#########################################################
#Hyperparameters
boost_clf2=GradientBoostingClassifier(learning_rate=0.02,n_estimators=1000,max_depth=1)
boost_clf2.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#Evalution on testing data
confusion_matrix(y_test,boost_clf2.predict(X_test))
"""
array([[  0,  47],
       [  0, 353]], dtype=int64)
"""
accuracy_score(y_test,boost_clf2.predict(X_test))
#Out[37]: 0.8825

#Evalution on training data
accuracy_score(y_train,boost_clf2.predict(X_train))
#Out[38]: 0.851782363977486