# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:28:26 2024

@author: Paresh Dhamne

Problem:
    The head of HR of a certain organization wants to automate their salary hike estimation. 
    The organization consulted an analytics service provider and asked them to build a basic prediction model 
    by providing them with a dataset that contains the data about the number of years of experience and 
    the salary hike given accordingly. Build a Simple Linear Regression model with salary as the target variable. 
    Apply necessary transformations and record the RMSE and correlation coefficient values for different models.
    
Business Objective:
    
    Minimize: Minimizing the overestimation of salaries
              
    Maximize: employee satisfaction
    
Business Constraints:
    budget allocated for salary hikes and  availability and quality of data
    
    
DATA DICTIONARY:
    YearsExperience: No of experience employee has
    Salary: Salaey based on experience per year
"""


import pandas as pd 
import numpy as np 
import seaborn as sns
from sklearn import linear_model 
import matplotlib.pyplot as plt

data=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Regression/Datasets_SLR(1)/Salary_Data.csv")
data
##################################################################

data.columns
#Out[8]: Index(['YearsExperience', 'Salary'], dtype='object')
###################################################################

data.shape
#Out[9]: (30, 2)
##############################################################
data.size
#Out[10]: 60
################################################################
data.dtypes
'''
Out[11]: 
YearsExperience    float64
Salary             float64
dtype: object
'''
#############################################################
data.isnull().sum()
'''
Out[16]: 
YearsExperience    0
Salary             0
dtype: int64

There is no null value in given data
'''
#########################################################################
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 2 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   YearsExperience  30 non-null     float64
 1   Salary           30 non-null     float64
dtypes: float64(2)
memory usage: 612.0 bytes
'''
#########################################################################
data.describe()
'''
Out[18]: 
       YearsExperience         Salary
count        30.000000      30.000000
mean          5.313333   76003.000000
std           2.837888   27414.429785
min           1.100000   37731.000000
25%           3.200000   56720.750000
50%           4.700000   65237.000000
75%           7.700000  100544.750000
max          10.500000  122391.000000
#it will provide 5 number summary of dataset
'''
#########################################################################

#Boxplot
sns.boxplot(x=data["YearsExperience"])
sns.boxplot(x=data["Salary"])
#there are no outliers are present in given data
#########################################################

#Draw scatter plot 
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.scatter(data['YearsExperience'],data['Salary'],color='red',marker='+')
#most of the delivery time is between 15 to 20 and sorting time between 5 to 8
#######################################################################

#get target variable
new_df=data.drop('Salary',axis='columns')
new_df

Salary=data['Salary']
Salary

##################################################################3
#create linear regression model
reg= linear_model.LinearRegression()
reg.fit(new_df,Salary)

#predict calories used for weight gained
reg.predict([[9.6]])
#Out[28]: array([116511.83848464])

#coefficeint of regression
reg.coef_
#Out[29]: array([9449.96232146])

reg.intercept_
#Out[30]: 25792.20019866871

#Equation of simple regular expression
#y=m*X+b

y=9.6*reg.intercept_+reg.coef_
y
#Out[32]: array([257055.08422867])
#########################################################################
# 30
reg.predict([[10.5]])
#########################################################################

from sklearn.metrics import mean_squared_error, r2_score

# Predict Salary based on experience
Salary_predicted = reg.predict(new_df)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(Salary, Salary_predicted))
print("Root Mean Squared Error (RMSE):", rmse)
#Root Mean Squared Error (RMSE): 5592.043608760662
# the difference between the actual calories consumed and the predicted calories
# consumed by the model is approximately 5592.043608760662
######################################################################

# Calculating correlation coefficient
correlation_coefficient = np.corrcoef(Salary, Salary)[0, 1]
print("Correlation Coefficient:", correlation_coefficient)
#Correlation Coefficient: 1.0
#given data has strong  positive linear regression
#######################################################################

# Evaluating the polynomial model
#poly_rmse = np.sqrt(mean_squared_error(y_test, poly_predictions))
#poly_r2 = r2_score(y_test, poly_predictions)
#print(f"Polynomial Model RMSE: {poly_rmse}") # 7247.6145295383185
#print(f"Polynomial Model R^2: {poly_r2}") # 7247.6145295383185
# As we can see that the log transformation  will give the best result so we will use same one

#################################################################################
'''
benefits/impact of the solution :
The automated salary hike estimation model optimizes budget utilization, 
enhances employee satisfaction, and fosters fair compensation practices, 
ultimately improving retention and competitiveness in talent acquisition.
'''









