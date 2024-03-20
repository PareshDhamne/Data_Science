# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:36:03 2023

@author: Hp
"""

#one hot encoder
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
#we use ethinic diversity dataset
df=pd.read_csv("D:/Datasets/ethnic diversity.csv")
df.columns
#we have salaries and age as numrical column, let us make them 
#at position 0 and 1 so to make further data processing easy

df=df[['Salaries','age','Position','State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus','Department']]
#check the datafrsame in variable explorer
#we want only nominal data and oridinal data for processing
#hence skipped 0 th and first column and applied  to one hot encoder
enc_df=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())
#transform dataframe column name is not their that is drawback of transform datafrsames
########################################################

#Label encoding
import pandas as pd
df=pd.read_csv("D:/Datasets/ethnic diversity.csv")
from sklearn.preprocessing import LabelEncoder
#creating instance of label encoder
labelencoder = LabelEncoder()
#split your data into input and output variables
x=df.iloc[:,0:9]
y=df['Race']
df.columns
#we have nominal data sex,MaritalDesc,CitizenDesc,
#we want to convert to label encoder

x['Sex']=labelencoder.fit_transform(x['MaritalDesc'])
x['MAritalDesc']=labelencoder.fit_transform(x['CitizenDesc'])
#label encoder y
y=labelencoder.fit_transform(y)
df_new=pd.concat([x,y],axis=1)
#if you will see variable explorer, y do not have column name
#hence remove the column
df_new=df_new.rename(columns={0:'Race'})
######################################################

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("D:/Datasets/mtcars.csv")
d.describe()
a=d.describe()
##initialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()
#here if you will check res, in variable environment then you will find



###########################################################




k=pd.read_csv("D:/Datasets/Seeds_data.csv")
k.describe()
b=k.describe()
scalar=StandardScaler()
df=scalar.fit_transform(k)
dataset=pd.DataFrame(df)
res=dataset.describe()
#####################################################
#normalization
ethnic=pd.read_csv("D:/Datasets/ethnic diversity.csv")
#now read columns
ethnic.columns
#there are some columns which not useful we need to drop
ethnic.drop(['Employee_Name','EmpID','Zip'],axis=1,inplace=True)
#now read minimum value and maximumvalues of salaries and age
a1=ethnic.describe()
#check a1 data frame in variable explorer
#you find minimum salary is 0 and max is 108304
#same way check for age, there is huge difference 
#in min and max.value. Hence we are going for  normalization
#first we will have to convert non_numeric dsta in label encoding

ethnic=pd.get_dummies(ethnic,drop_first=True)
#normalization function weitten where ethinic argument is passed
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
df_norm=norm_func(ethnic)
b=df_norm.describe()
#if you will observe the b frame,
#it has dimensions 8,81
#earlier in a thery were 8,11 it is because all non_numeric
#data has been converted to numeric using label encoding