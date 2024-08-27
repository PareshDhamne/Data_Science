# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:16:01 2024

@author: Paresh Dhamne

Problem: A certain food-based company conducted a survey with the help of a fitness company 
to find the relationship between a person’s weight gain and the number of calories they consumed in order 
to come up with diet plans for these individuals. 
Build a Simple Linear Regression model with calories consumed as the target variable. 
Apply necessary transformations and record the RMSE and correlation coefficient values for different models. 

Business Objective:
    
    Minimize: Minimizing the discrepancy between predicted and actual calorie consumption 
             helps prevent dissatisfaction among customers 
             
    Maximize: Customer satisfaction
    
Business Constraints:
    Ensure that the data collected from individuals for the survey is handled ethically and in 
    compliance with data privacy regulations. 
    
    
DATA DICTIONARY:
    
Weight_gained_(grams) : Column gives the weight of the person in grams which is numerical data
Calories_Consumed : Column gives the calories consumed to reduce weight which is numerical data
    
"""

import pandas as pd 
import numpy as np 
import seaborn as sns
from sklearn import linear_model 
import matplotlib.pyplot as plt

data=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Regression/Datasets_SLR(1)/calories_consumed.csv")
data
##################################################################

#Rename the column name
data.columns=data.columns.str.replace(' ', '_')
data.columns
###################################################################

data.shape
#Out[10]: (14, 2)
#############################################################

data.size
#Out[11]: 28
##############################################################

data.dtypes
'''
Out[52]: 
Weight_gained_(grams)    int64
Calories_Consumed        int64
dtype: object
'''
##################################################################
data.sum().isnull()
'''
#Out[12]: 
Weight_gained_(grams)    False
Calories_Consumed        False
dtype: bool
data.describe()

There is no null value in given data
'''
#########################################################################

data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 14 entries, 0 to 13
Data columns (total 2 columns):
 #   Column                 Non-Null Count  Dtype
---  ------                 --------------  -----
 0   Weight_gained_(grams)  14 non-null     int64
 1   Calories_Consumed      14 non-null     int64
dtypes: int64(2)
memory usage: 356.0 bytes
'''
##################################################################

data.describe()
'''
       Weight_gained_(grams)  Calories_Consumed
count              14.000000          14.000000
mean              357.714286        2340.714286
std               333.692495         752.109488
min                62.000000        1400.000000
25%               114.500000        1727.500000
50%               200.000000        2250.000000
75%               537.500000        2775.000000
max              1100.000000        3900.000000
#it will provide 5 number summary of dataset
'''
####################################################################

#Boxplot
sns.boxplot(x=data["Weight_gained_(grams)"])
sns.boxplot(x=data["Calories_Consumed"])
#there are no outliers are present in given data
#########################################################

#Draw scatter plot 
plt.xlabel('Weight_gained_(grams)')
plt.ylabel('Calories_Consumed')
plt.scatter(data['Weight_gained_(grams)'],data['Calories_Consumed'],color='red',marker='+')
#most of the weight gain is between 0 to 400gm and calories consumed upto 2500
#######################################################################

#get target variable
new_df=data.drop('Calories_Consumed',axis='columns')
new_df

calories=data['Calories_Consumed']
calories

##################################################################3
#create linear regression model
reg= linear_model.LinearRegression()
reg.fit(new_df,calories)

#predict calories used for weight gained
reg.predict([[250]])

#coefficeint of regression
reg.coef_
#Out[27]: array([2.13442296])

reg.intercept_
#Out[28]: 1577.2007020291894

#Equation of simple regular expression
#y=m*X+b

y=250*reg.intercept_+reg.coef_
y
#Out[30]: array([394302.30993025])
#########################################################################
# 290
reg.predict([[290]])
#########################################################################

from sklearn.metrics import mean_squared_error, r2_score

# Predicting calories consumed based on weight gained
calories_predicted = reg.predict(new_df)

# Calculating RMSE
rmse = np.sqrt(mean_squared_error(calories, calories_predicted))
print("Root Mean Squared Error (RMSE):", rmse)
#Root Mean Squared Error (RMSE): 232.8335007096089
# the difference between the actual calories consumed and the predicted calories
# consumed by the model is approximately 232.83 units
######################################################################

# Calculating correlation coefficient
correlation_coefficient = np.corrcoef(calories, calories_predicted)[0, 1]
print("Correlation Coefficient:", correlation_coefficient)
#Correlation Coefficient: 0.9469910088554458
#given data has  positive linear regression
#######################################################################
'''
benefits/impact of the solution :
#The solution empowers the food-based company to provide personalized diet plans, 
#boosting customer satisfaction and brand reputation while adhering to ethical data practices, 
#ultimately leading to improved health outcomes and competitive advantage.
'''





