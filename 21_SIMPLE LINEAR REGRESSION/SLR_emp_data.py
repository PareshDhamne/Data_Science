# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:50:12 2024

@author: Paresh Dhamne
Problem:
    A certain organization wants an early estimate of their employee churn out rate. 
    So the HR department gathered the data regarding the employee’s salary hike and the churn out rate in a financial year. 
    The analytics team will have to perform an analysis and predict an estimate of employee churn based on the salary hike. 
    Build a Simple Linear Regression model with churn out rate as the target variable. 
    Apply necessary transformations and record the RMSE and correlation coefficient values for different models.
    
Business Objective:
    
    Minimize: Minimizing employee churn is essential for maintaining workforce stability, productivity, and morale. 
              
    Maximize: The company can implement retention strategies to maximize employee retention and reduce turnover costs.
    
Business Constraints:
    Ensure that the model's predictions are based on ethical data practices, 
    maintaining confidentiality and privacy of employee information and salary data.
    
DATA DICTIONARY:
    Salary_hike: column records the percentage increase in salary granted to employees within a financial year
    Churn_out_rate: column denotes the proportion or rate at which employees leave the organization within the same financial year
"""


import pandas as pd 
import numpy as np 
import seaborn as sns
from sklearn import linear_model 
import matplotlib.pyplot as plt

data=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Regression/Datasets_SLR(1)/emp_data.csv")
data
##################################################################

data.columns
#Out[8]: Index(['Salary_hike', 'Churn_out_rate'], dtype='object')
###################################################################

data.shape
#Out[16]: (10, 2)
##############################################################
data.size
#Out[11]: 20
################################################################
data.dtypes
'''
Out[11]: 
Salary_hike       int64
Churn_out_rate    int64
dtype: object
'''
#############################################################
data.isnull().sum()
'''
Salary_hike       0
Churn_out_rate    0
dtype: int64

There is no null value in given data
'''
#########################################################################
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 2 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Salary_hike     10 non-null     int64
 1   Churn_out_rate  10 non-null     int64
dtypes: int64(2)
memory usage: 292.0 bytes
'''
#########################################################################
data.describe()
'''
Out[15]: 
       Salary_hike  Churn_out_rate
count    10.000000       10.000000
mean   1688.600000       72.900000
std      92.096809       10.257247
min    1580.000000       60.000000
25%    1617.500000       65.750000
50%    1675.000000       71.000000
75%    1724.000000       78.750000
max    1870.000000       92.000000
#it will provide 5 number summary of dataset
'''
#########################################################################

#Boxplot
sns.boxplot(x=data["Salary_hike"])
sns.boxplot(x=data["Churn_out_rate"])
#there are no outliers are present in given data
#########################################################

#Draw scatter plot 
plt.xlabel('Salary_hike')
plt.ylabel('Churn_out_rate')
plt.scatter(data['Salary_hike'],data['Churn_out_rate'],color='red',marker='+')
#most of the Salary_hike is between 1600 to 1750 and sorting time between 65 to 75
#######################################################################

#get target variable
new_df=data.drop('Churn_out_rate',axis='columns')
new_df

Churn_out_rate=data['Churn_out_rate']
Churn_out_rate

##################################################################3
#create linear regression model
reg= linear_model.LinearRegression()
reg.fit(new_df,Churn_out_rate)

#predict calories used for weight gained
reg.predict([[1580]])
#Out[26]: array([83.9275313])

#coefficeint of regression
reg.coef_
#array([-0.10154265])

reg.intercept_
#Out[29]: 244.36491110400797

#Equation of simple regular expression
#y=m*X+b

y=1580*reg.intercept_+reg.coef_
y
#Out[39]: array([67.47635962])
#########################################################################
# 1730
reg.predict([[1730]])
#########################################################################

from sklearn.metrics import mean_squared_error, r2_score

# Predict delivery time based on sorting time
Churn_out_rate_predicted = reg.predict(new_df)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(Churn_out_rate, Churn_out_rate_predicted))
print("Root Mean Squared Error (RMSE):", rmse)
#Root Mean Squared Error (RMSE): 3.9975284623377942
# the difference between the actual calories consumed and the predicted calories
# consumed by the model is approximately 3.9975284623377942
######################################################################

# Calculating correlation coefficient
correlation_coefficient = np.corrcoef(Churn_out_rate, Churn_out_rate_predicted)[0, 1]
print("Correlation Coefficient:", correlation_coefficient)
#Correlation Coefficient: 0.9117216186909111
#given data has  positive linear regression
#######################################################################
'''
benefits/impact of the solution :
The provided solution enables proactive identification of potential employee churn based on salary hike, 
leading to cost savings through targeted retention strategies and improved workforce stability.
'''








