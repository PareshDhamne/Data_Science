# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:35:13 2024

@author: Paresh Dhamne

Business Objective:

        Maximize: Improve the model's ability to accurately classify individuals into taxable and non-taxable income categories.

        Minimize: Reduce the occurrences of incorrectly predicting taxable or non-taxable income, as these errors may have different implications.

Business Contraints : 
        Ensure the decision tree model remains interpretable, allowing stakeholders to understand the factors influencing taxability predictions.

        
DATA DICTIONARY:

'Undergrad': Indicates whether an individual is pursuing undergraduate studies.
'Marital.Status': Specifies the marital status of an individual.
'Taxable.Income': Represents the income subject to taxation.
'City.Population': Refers to the population size of the city where an individual resides.
'Work.Experience': Denotes the number of years an individual has been employed or has relevant work experience.
'Urban': Indicates whether an individual resides in an urban area.
"""
####################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("D:/SUPERVISED ALGORTIHM/DECISION TREE/Fraud_check.csv")

df.head(10)

# 5 number summary
df.describe()

df.shape
# 600 rows and 6 columns

df.columns
'''
['Undergrad', 'Marital.Status', 'Taxable.Income', 'City.Population',
'Work.Experience', 'Urban']
'''

# check for null values
df.isnull()
# False
df.isnull().sum()
# 0 no null values

# Pair-Plot
plt.close();
sns.set_style("whitegrid");
sns.pairplot(df);
plt.show()

#####################
#rename the column
df.columns = [
    'Undergrad',
    'Marital_Status',
    'Income',
    'Population',
    'Experience',
    'Urban'
]

# Now you can access the columns
print(df.columns)

# boxplot
# boxplot on Income column
sns.boxplot(df.Income)
# In Income column 1 outliers 

sns.boxplot(df.Population)
# In Population column no outliers

# boxplot on df column
sns.boxplot(df)
# There is outliers on all columns

# histplot - show distributions of datasets
sns.histplot(df['Income'],kde=True)
# right skew and the distributed

sns.histplot(df['Population'],kde=True)
# right skew and the distributed

sns.histplot(df,kde=True)
#The data is showing the skewness 
# most of the right skiwed data

# Data Preproccesing
df.dtypes
# Some columns in int data types and some Object

# Identify the duplicates
duplicate=df.duplicated()
# Output of this function is single columns
# if there is duplicate records output- True
# if there is no duplicate records output-False
# Series is created
duplicate
# False
sum(duplicate)
# sum is 0.
# Normalize data 
# Normalize the data using norm function
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
# Apply the norm_fun to data 
df1=norm_fun(df.iloc[:,2:5])
df1
#####################################
#We merge the all the column in the df1 dataset 
df['Undergrad']
df1['Undergrad']=df['Undergrad']

df['Marital_Status']
df1["Marital_Status"]=df["Marital_Status"]

df["Urban"]
df1["Urban"]=df["Urban"]


#########################################
df.isnull().sum()
df.dropna()
df.columns
#########################################
# Converting into binary
lb=LabelEncoder()
df1["Undergrad"]=lb.fit_transform(df1["Undergrad"])
df1["Marital_Status"]=lb.fit_transform(df1["Marital_Status"])
df1["Urban"]=lb.fit_transform(df1["Urban"])

df1["Urban"].unique()
df1['Urban'].value_counts()
colnames=list(df1.columns)

predictors=colnames[:5]
target=colnames[5]

# Spliting data into training and testing data set
from sklearn.model_selection import train_test_split
train,test=train_test_split(df1,test_size=0.3)

from sklearn.tree import DecisionTreeClassifier as DT

model=DT(criterion='entropy')
model.fit(train[predictors], train[target])
preds_test=model.predict(test[predictors])
preds_test
pd.crosstab(test[target], preds_test,rownames=['Actual'],colnames=['predictions'])
np.mean(preds_test==test[target])

# Now let us check accuracy on training dataset
preds_train=model.predict(train[predictors])
pd.crosstab(train[target], preds_train,rownames=['Actual'],colnames=['predictions'])
np.mean(preds_train==train[target])

# 100 % accuracy 
# Accuracy of train data > Accuracy test data i.e Overfit model
