# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:15:03 2024

@author: PARESH DHAMNE

Business Objective:
    
        Maximize : The positive review and rating of the product related to the chocolate
        so thats why we have to improve the acccuracy factors i.e review
            
        Minimize : The negative reviews to the product as well as the cost requiered
        for the product

Business contraints : 
        The resources from where we collect the reviews of the product and also the security 
        of the informations so the custoner trust and satisfaction should be maintain.

#DATA DICTIONARY

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
###############################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from scipy.stats import skew

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

data=pd.read_excel("D:/12-SUPERVISED ALGORTIHM/ADABOOST/Coca_Rating_Ensemble.xlsx")

data['Rating_catogorical'] = pd.qcut(data['Rating'], q=2, labels=['Good', 'bad'])

data
'''
Out[13]: 
       Company                Name  ...    Origin  Rating_catogorical
0     A. Morin         Agua Grande  ...  Sao Tome                 bad
1     A. Morin               Kpime  ...      Togo                Good
2     A. Morin              Atsane  ...      Togo                Good
3     A. Morin               Akata  ...      Togo                 bad
4     A. Morin              Quilla  ...      Peru                 bad
       ...                 ...  ...       ...                 ...
1790    Zotter                Peru  ...      Peru                 bad
1791    Zotter               Congo  ...     Congo                Good
1792    Zotter        Kerala State  ...     India                 bad
1793    Zotter        Kerala State  ...     India                Good
1794    Zotter  Brazil, Mitzi Blue  ...    Brazil                Good

[1795 rows x 10 columns]
'''
###############################################################################

#Data information
data.head()
'''
Out[14]: 
    Company         Name   REF  ...  Bean_Type    Origin Rating_catogorical
0  A. Morin  Agua Grande  1876  ...             Sao Tome                bad
1  A. Morin        Kpime  1676  ...                 Togo               Good
2  A. Morin       Atsane  1676  ...                 Togo               Good
3  A. Morin        Akata  1680  ...                 Togo                bad
4  A. Morin       Quilla  1704  ...                 Peru                bad

[5 rows x 10 columns]
'''
###############################################################################

data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1795 entries, 0 to 1794
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype   
---  ------              --------------  -----   
 0   Company             1795 non-null   object  
 1   Name                1795 non-null   object  
 2   REF                 1795 non-null   int64   
 3   Review              1795 non-null   int64   
 4   Cocoa_Percent       1795 non-null   float64 
 5   Company_Location    1795 non-null   object  
 6   Rating              1795 non-null   float64 
 7   Bean_Type           1794 non-null   object  
 8   Origin              1794 non-null   object  
 9   Rating_catogorical  1795 non-null   category
dtypes: category(1), float64(2), int64(2), object(5)
memory usage: 128.2+ KB
'''
###############################################################################

data.isna().sum()
'''
Out[16]: 
Company               0
Name                  0
REF                   0
Review                0
Cocoa_Percent         0
Company_Location      0
Rating                0
Bean_Type             1
Origin                1
Rating_catogorical    0
dtype: int64
#There is  null value present in column Bean_Type, Origin in given dataset
'''
###############################################################################

#EDA
target=data["Rating_catogorical"]
sns.countplot(x=target,palette='winter')
plt.xlabel("Coca_rating")
#our data is evenly distributed. Atleast 600 are there in both choise
plt.figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True, cmap='YlGnBu',fmt='.2f')

#observations

#1) REF ,Review are highly correlated to each other
##############################################################################

sns.set_context('notebook', font_scale=1.2)
fig,ax=plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of cocoa bean production based on Rating_catogorical',fontsize=20)

ax1=sns.histplot(x='REF',data=data,hue='Rating_catogorical',kde=True,ax=ax[0],palette='winter')
ax1.set(xlabel='REF',title='Distribution of cocoa bean production based on Rating_catogorical')

ax2=sns.histplot(x='Cocoa_Percent',data=data,hue='Rating_catogorical',kde=True,ax=ax[1],palette='coolwarm')
ax2.set(xlabel='Cocoa_Percent',title='Distribution of cocoa bean production based on Rating_catogorical')

plt.show()
###############################################################################

data.hist(bins=30,figsize=(20,15),color='#005b96');

#As we cans ee there are outliers in Cocoa_Percent

sns.boxplot(x=data["Coca_Percent"])

###############################################################################

#checking skewness

skew_df=pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew']=skew_df['Feature'].apply(lambda feature:skew(data[feature]))
skew_df['Absolute Skew']=skew_df['Skew'].apply(abs)
skew_df['Skewed']=skew_df['Absolute Skew'].apply(lambda x: True if x>0.5 else False)
skew_df
'''
ut[24]: 
         Feature      Skew  Absolute Skew  Skewed
0            REF -0.141338       0.141338   False
1         Review -0.526794       0.526794    True
2  Cocoa_Percent  1.057719       1.057719    True
3         Rating -0.578447       0.578447    True
#Cocoa_Percent column is clearly skewed as we also saw in the histogram
'''
###############################################################################

for column in skew_df.query("Skewed==True")['Feature'].values:data[column]=np.log1p(data[column])

data.head()
'''
Out[26]: 
    Company         Name   REF  ...  Bean_Type    Origin Rating_catogorical
0  A. Morin  Agua Grande  1876  ...             Sao Tome                bad
1  A. Morin        Kpime  1676  ...                 Togo               Good
2  A. Morin       Atsane  1676  ...                 Togo               Good
3  A. Morin        Akata  1680  ...                 Togo                bad
4  A. Morin       Quilla  1704  ...                 Peru                bad

[5 rows x 10 columns]
'''
###############################################################################

#Encoding
data1=data.copy()
data1=pd.get_dummies(data1)
data1.head()
'''
Out[29]: 
    REF    Review  ...  Rating_catogorical_Good  Rating_catogorical_bad
0  1876  7.609367  ...                        0                       1
1  1676  7.608871  ...                        1                       0
2  1676  7.608871  ...                        1                       0
3  1680  7.608871  ...                        0                       1
4  1704  7.608871  ...                        0                       1
'''
##############################################################################

#Scaling
data2 = data1.copy()
sc=StandardScaler()
data2[data1.select_dtypes(np.number).columns]=sc.fit_transform(data2[data1.select_dtypes(np.number).columns])
data2.drop(['Rating_catogorical_Good'],axis=1,inplace=True)
data2.head()
'''
Out[34]: 
        REF    Review  ...  Origin_   Rating_catogorical_bad
0  1.519895  1.254792  ... -0.205895                1.247790
1  1.158056  0.913744  ... -0.205895               -0.801417
2  1.158056  0.913744  ... -0.205895               -0.801417
3  1.165293  0.913744  ... -0.205895                1.247790
4  1.208714  0.913744  ... -0.205895                1.247790
'''
###############################################################################

from sklearn.preprocessing import LabelEncoder
le__Class_variable=LabelEncoder()

data['Rating_catogorical']= le__Class_variable.fit_transform(data['Rating_catogorical'])
data

#Splitting
data_f=data2.copy()
target=data['Rating_catogorical']
target=target.astype(int)
target

X_train,X_test,y_train,y_test=train_test_split(data_f,target,test_size=0.2,stratify=target,random_state=42)
##############################################################################

#Modeling
from sklearn.ensemble import  AdaBoostClassifier

ad_clf=AdaBoostClassifier(learning_rate=0.02,n_estimators=5000)
ad_clf.fit(X_train,y_train)
#Out[46]: AdaBoostClassifier(learning_rate=0.02, n_estimators=5000)
##############################################################################

from sklearn.metrics import accuracy_score,confusion_matrix

#Evaluation on testing data
confusion_matrix(y_test, ad_clf.predict(X_test))
'''
Out[48]: 
array([[219,   0],
       [  0, 140]], dtype=int64)
'''

accuracy_score(y_test, ad_clf.predict(X_test))
##############################################################################

#Evalution on Training data
accuracy_score(y_train,ad_clf.predict(X_train))

##############################################################################

