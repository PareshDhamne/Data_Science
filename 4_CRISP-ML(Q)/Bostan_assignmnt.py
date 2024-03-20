# -*- coding: utf-8 -*-
"""

Objectives:
    Minimize: reduce the rate of crime in the down
    Maximize: Increase the proportion of non_retail businesss by increasing the number of opportunites to the lower status of the popi]ulation

Business constraints:Ensure that all lower status population will get some work and will help to increase the business by providing them good facilities.

Dataset: Boston
This dataset contains information collected by the U.S. Census Service concerning housing in the area of Boston,Massachusetts. 
The dataset has 506 rows, each representing a different house in the area. 
There are 14 columns, each representing a different aspect of the houses and their surroundings. 
Following is the details of the columns:

crim: This is the per capita crime rate by town.
zn: This is the proportion of residential land zoned for lots over 25,000 sq.ft.
indus: This is the proportion of non-retail business acres per town.
chas: This is a Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
nox: This is the nitric oxides concentration (parts per 10 million).
rm: This is the average number of rooms per dwelling.
age: This is the proportion of owner-occupied units built prior to 1940.
dis: This is the weighted distances to five Boston employment centers.
rad: This is the index of accessibility to radial highways.
tax: This is the full-value property-tax rate per $10,000.
ptratio: This is the pupil-teacher ratio by town.
b: This is calculated as 1000(Bk – 0.63)^2, where Bk is the proportion of people of African American descent by town.
lstat: This is the percentage lower status of the population.
medv: This is the median value of owner-occupied homes in $1000s and is often the target variable in regression problems.

"""

from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("D:/Datasets/Boston.csv")
df

###########################################

df.shape
###########################################
df.columns
###########################################
df.describe()
###########################################
df.dtypes
###########################################
df.isnull()
###########################################
duplicate=df.duplicated()
duplicate
sum(duplicate)
###########################################
#Boxplot
sns.boxplot(df['crim'])
#it has outliers
sns.boxplot(df['zn'])
#it has outliers
sns.boxplot(df['indus'])
#it doesnt have outlirers
sns.boxplot(df['chas'])
#it has outliers
sns.boxplot(df['nox'])
#it doesnt have outlirers
sns.boxplot(df['rm'])
#it has outliers
sns.boxplot(df['age'])
#it doesnt have outlirers
sns.boxplot(df['dis'])
#it has outliers
sns.boxplot(df['rad'])
#it doesnt have outlirers
sns.boxplot(df['tax'])
#it doesnt have outlirers
sns.boxplot(df['ptratio'])
#it has outliers
sns.boxplot(df['b'])
sns.boxplot(df['lstat'])
#it has outliers
sns.boxplot(df['medv'])
#it has outliers
#############################################

#outliers tretment
sns.boxplot(df['crim'])
IQR=df.crim.quantile(0.75)-df.crim.quantile(0.25)
IQR

lower_limit=df.crim.quantile(0.25)-1.5*IQR
upper_limit=df.crim.quantile(0.75)+1.5*IQR
#Trimming
outliers_df=np.where(df.crim>upper_limit,True,np.where(df.crim<lower_limit,True,False))
df_trimmed=df.loc[~outliers_df]
df.shape
df_trimmed.shape
