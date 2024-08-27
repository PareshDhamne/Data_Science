# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 23:07:35 2024

@author: Paresh Dhamne

Business Objective:
    
        Maximize : The positive review and rating of the product related to the chocolate
        so thats why we have to improve the acccuracy factors i.e review
            
        Minimize : The negative reviews to the product as well as the cost requiered
        for the product

Business contraints : 
        The resources from where we collect the reviews of the product and also the security 
        of the informations so the custoner trust and satisfaction should be maintain.

Company: Name of the chocolate company.
Name: Name of the chocolate product.
REF: Reference number or identifier for each chocolate product.
Review: Review metric or score for each chocolate product.
Cocoa_Percent: Percentage of cocoa in each chocolate product.
Company_Location: Location of the chocolate company.
Rating: Numerical rating for each chocolate product.
Bean_Type: Type of cocoa bean used in each chocolate product.
Origin: Origin of the cocoa beans used in each chocolate product.
Rating_catogorical: Categorical ratings for each chocolate product.
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

data=pd.read_excel("D:/12-SUPERVISED ALGORTIHM/GRADIENT BOOSTING/Coca_Rating_Ensemble.xlsx")

data['Rating_catogorical'] = pd.qcut(data['Rating'], q=2, labels=['Good', 'bad'])

data
################################################################################################

#Data information
data.head()
data.info()
data.isna().sum()
#There is  null value present in column Bean_Type, Origin in given dataset
########################################################################################################

#EDA
target=data["Rating_catogorical"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Coca_rating")
#our data is evenly distributed. Atleast 600 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#observations

#1) REF ,Review are highly correlated to each other

################################################################################################
sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of cocoa bean production based on Rating_catogorical',fontsize=20)

ax1=sns.histplot(x='REF',data=data,hue='Rating_catogorical',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='REF',title='Distribution of cocoa bean production based on Rating_catogorical')

ax2=sns.histplot(x='Cocoa_Percent',data=data,hue='Rating_catogorical',kde=True,ax=ax[1],palette='coolwarm')
ax2.set(xlabel='Cocoa_Percent',title='Distribution of cocoa bean production based on Rating_catogorical')

plt.show()
##########################################################################################

data.hist(bins=30,figsize=(20,15),color='#005b96');

#As we cans ee there are outliers in Cocoa_Percent
#######################################################################
sns.boxplot(x=data["Coca_Percent"])

###########################################################################

#checking skewness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df

#Cocoa_Percent column is clearly skewed as we also saw in the histogram

for column in skew_df.query("Skewed==True")['Feature'].values:data[column]=np.log1p(data[column])

######################################################################################

#dummy variables
data.head()
data.info()

#n-1 dummy variables will be created for n categories


data=pd.get_dummies(data,columns=["Company","Name","Company_Location","Bean_Type","Origin"],drop_first=True)
data.drop("Rating",axis=1)
data.head()

#Input and output Split
predictors = data.loc[:,data.columns!="Rating_catogorical"]
type(predictors)

target=data["Rating_catogorical"]

#Train Test partition of the data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)

from sklearn.ensemble import GradientBoostingClassifier
boost_clf=GradientBoostingClassifier()
boost_clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

confusion_matrix(y_test,boost_clf.predict(X_test))
'''
array([[216,   0],
       [  0, 143]], dtype=int64)
'''

accuracy_score(y_test,boost_clf.predict(X_test))

#Hyperparameters
boost_clf2=GradientBoostingClassifier(learning_rate=0.02,
                                        n_estimators=1000,
                                        max_depth=1)
boost_clf2.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#Evalution on testing data
confusion_matrix(y_test,boost_clf2.predict(X_test))
accuracy_score(y_test,boost_clf2.predict(X_test))

#Evalution on training data
accuracy_score(y_train,boost_clf2.predict(X_train))
