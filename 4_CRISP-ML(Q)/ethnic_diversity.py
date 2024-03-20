# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:32:09 2023

@author: Paresh Dhamne
"""
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv("D:/Datasets/ethnic diversity.csv")
df
######################################
df.shape
########################################
df.columns
####################################
df.dtypes
#salaries data type is flaot, let us convet into int
###################################
df.isnull()
###################################
df.Salaries=df.Salaries.astype(int)
df.dtypes
#now the data typwe of salaries is int
#similarly age data type must be flaot
#present it is int
df.age=df.age.astype(float)
df.dtypes
####################################

#2)identify the duplicates
df_new=pd.read_csv("D:/Datasets/education.csv")
duplicate=df_new.duplicated()
#output of this function is single column
#if there is duplicate records output-true
#if there is no duplicate records output-False
#series will be created
duplicate
sum(duplicate)
#output will be zero

#now lets import another dataset
df_new1=pd.read_csv("D:/Datasets/mtcars_dup.csv")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)
#There are 3 duplicate records
#row 17 is duplicate of row 2 like wise you 

df_new2=df_new1.drop_duplicates()
duplicate2=df_new2.duplicated()
duplicate2
sum(duplicate2)

########################################

#3) outliers tretment
import pandas as pd
import seaborn as sns
df=pd.read_csv("D:/Datasets/ethnic diversity.csv")

#now let us find outliers in salaries
sns.boxplot(df.Salaries)
#there are outliers
#let us calculate IQR

IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have obeseved IQR in variable explorer
#no because IQR is in capital letters
#treated as constant
IQR
#but if we will try as I,Iqr or iqr then it is showing
#I=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#Iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)

lower_limit=df.Salaries.quantile(0.25)-1.5*IQR
upper_limit=df.Salaries.quantile(0.75)+1.5*IQR
#now if you will check the lower limit of
#slary it is -19446.9675
#there is negative salary
#so make it as 0
#############################################

#4) Trimming
import numpy as np
outliers_df=np.where(df.Salaries>upper_limit,True,np.where(df.Salaries<lower_limit,True,False))
#if our df.salaries is greater than upper limit then there is outlier and return true and samif less than lower_limit return True else return False
 #you can check outliers_df column in variable explorer
df_trimmed=df.loc[~outliers_df]
df.shape
df_trimmed.shape
###########################################

#5) Replacemet Technique
#Drawback  of trimming technique is we are losing the data
df=pd.read_csv("D:/Datasets/ethnic diversity.csv")
df.describe

#record no.23 has got outliers
#map all the outliers values to upper limit
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
#if the values are greater than upper_limit
#map it to upper limit,a dn less than lower limit
#map it to lower limit, if it is within the range
#then kepp as it is
sns.boxplot(df_replaced[0])
######################################################

# 6. Winsorizor

from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['Salaries'])


df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])
######################################################

#7) zero varience aand near zero varience
#if there is no variance in the feature, then ML module
#will not get any intelligence, so it is better to ignore those features
import pandas as pd
df=pd.read_csv("D:/Datasets/ethnic diversity.csv")
df.var()
#here EmpID and ZIP is nominal data
#salary has  4.441953e+08 is 4441953000 which is
#close to 0
#similarly age 8.571358e+01
#both the features are having considarable Variance

df.var()==0

df.var(axis=0)==0
#########################################################
#8. Discritzation or Binning

import pandas as pd
import numpy as np

data=pd.read_csv('D:/Datasets/ethnic diversity.csv')
data

data.head()

data.info()
#it gives size,null values,data types,rows,columns,and column dat

data.describe()
#applicable only for numerical columns

#Uniform Stratergy
data['Salaries_new']=pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.mean(),max(data.Salaries)],labels=['low','high'])
data.Salaries_new.value_counts()

# Quantile Stratergy
data['Salaries_new']=pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.quantile(0.25),data.Salaries.mean(),data.Salaries.quantile(0.75),max(data.Salaries)],labels=['grp1','grp2','grp3','grp4'])
data.Salaries_new.value_counts()

#It will categorize the data present in columns with the labels by 
# matching the labels then we will visulaize the data
###############################################################

# 9.  Dummy variable Creation
# we can convert nominal data and  ordinal data into dummy variable

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('animal_category.csv')
df.shape

df.drop(['Index'],axis=1,inplace=True)

df

df_new=pd.get_dummies(df)
#It will create dummy columns and convert it into numerical value

df_new.shape

# we are geting two columns for homely and gender ,so we can delete one 
# column from both

df_new.drop(['Gender_Male','Homly_Yes'],axis=1,inplace=True)
df_new.shape


df_new.rename(columns={'Gender_Female':'Gender','Homly_No':'Homly'})
#############################
#Use of ethnic dataset 

df=pd.read_csv('ethnic diversity.csv')
df.shape

df.head()
df.columns
df.dtypes

df.drop(['EmpID','Salaries','age'],axis=1,inplace=True)
 # we have to drop the three columns because they already in numeric form
 
df_new=pd.get_dummies(df)
df_new.columns
df_new.shape

###############################################################################

# 10. One hot encoding

import pandas as pd

from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
df=pd.read_csv('ethnic diversity.csv')
df.columns

#We have salaries and age column in numeric form thenrearrange it 
# so we can preprocess further

df=df[['Salaries','age','Position','State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus','Race','Employee_Name','EmpID','Zip','Department']]

# we want only nominal and ordinal data for preprocessing so we exclude the 
#  alredy nummeric form column 
enc_df=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())
enc_df.columns

######################################################################################

# 11. label Encoder 
# in this we have to convert the nominal and ordinal columns 
# into the numerical one by one 

from sklearn.preprocessing import LabelEncoder

labelencoder=LabelEncoder()

#split the data into imput and output variables
X=df.iloc[:,0:9]
y=df['Race']

df.columns

# we have sex ,maritaDesc,CitizenDesc column we want to convert to label encoder
X['Sex']=labelencoder.fit_transform(X['Sex'])
X['MaritalDesc']=labelencoder.fit_transform(X['MaritalDesc'])
X['CitizenDesc']=labelencoder.fit_transform(X['CitizenDesc'])

# label encodery
y=labelencoder.fit_transform(y)

# this is going to create an array we have to convert back
# into dataFrame

y=pd.DataFrame(y)

# conca the input and output variables

new_df=pd.concat([X,y],axis=1)

#if ypu explorer , y do not have column name
# hence rename the column

new_df= new_df.rename(columns={0:'Race'})

new_df

##################################################################################
