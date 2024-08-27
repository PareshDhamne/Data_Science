# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:48:09 2024

@author: Paresh Dhamne

Problem:
    A certain university wants to understand the relationship between students’ SAT scores and their GPA. 
    Build a Simple Linear Regression model with GPA as the target variable and 
    record the RMSE and correlation coefficient values for different models
    
Business Objective:
    
    Minimize:  Minimizing the gap between students' SAT scores and their GPA to ensure fair and 
               accurate assessment of academic performance.
              
    Maximize: Maximizing the predictive accuracy of the GPA model to provide students 
              with reliable feedback on their academic progress and potential areas for improvement.
    
Business Constraints:
    Ensure ethical data practices and confidentiality of student information.
   
DATA DICTIONARY:
    SAT_Scores: Sat score of the student
    GPA: GPA for given SAT score
"""


import pandas as pd 
import numpy as np 
import seaborn as sns
from sklearn import linear_model 
import matplotlib.pyplot as plt

data=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Regression/Datasets_SLR(1)/SAT_GPA.csv")
data
##################################################################

data.columns
#Out[47]: Index(['SAT_Scores', 'GPA'], dtype='object')
###################################################################

data.shape
#Out[48]: (200, 2)
##############################################################
data.size
#Out[10]: 400
################################################################
data.dtypes
'''
Out[50]: 
SAT_Scores      int64
GPA           float64
dtype: object
'''
#############################################################
data.isnull().sum()
'''
Out[52]: 
SAT_Scores    0
GPA           0
dtype: int64

There is no null value in given data
'''
#########################################################################
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 2 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   SAT_Scores  200 non-null    int64  
 1   GPA         200 non-null    float64
dtypes: float64(1), int64(1)
memory usage: 3.3 KB
'''
#########################################################################
data.describe()
'''
Out[54]: 
       SAT_Scores         GPA
count  200.000000  200.000000
mean   491.810000    2.849500
std    174.893834    0.541076
min    202.000000    2.000000
25%    349.750000    2.400000
50%    480.500000    2.800000
75%    641.500000    3.400000
max    797.000000    3.900000
#it will provide 5 number summary of dataset
'''
#########################################################################

#Boxplot
sns.boxplot(x=data["SAT_Scores"])
sns.boxplot(x=data["GPA"])
#there are no outliers are present in given data
#########################################################

#Draw scatter plot 
plt.xlabel('SAT_Scores')
plt.ylabel('GPA')
plt.scatter(data['SAT_Scores'],data['GPA'],color='red',marker='+')
#data is randomly spread
#######################################################################

#get target variable
new_df=data.drop('GPA',axis='columns')
new_df

GPA=data['GPA']
GPA

##################################################################3
#create linear regression model
reg= linear_model.LinearRegression()
reg.fit(new_df,GPA)

#predict calories used for weight gained
reg.predict([[259]])
#Out[64]: array([2.6380779])

#coefficeint of regression
reg.coef_
#Out[65]: array([0.00090813])

reg.intercept_
#Out[66]: 2.4028718310256174

#Equation of simple regular expression
#y=m*X+b

y=259*reg.intercept_+reg.coef_
y
#Out[68]: array([622.34471237])
#########################################################################
# 260
reg.predict([[260]])
#########################################################################

from sklearn.metrics import mean_squared_error, r2_score

# Predict Salary based on experience
GPA_predicted = reg.predict(new_df)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(GPA, GPA_predicted))
print("Root Mean Squared Error (RMSE):", rmse)
#Root Mean Squared Error (RMSE): 0.5159457227723684
# the difference between the actual calories consumed and the predicted calories
# consumed by the model is approximately 0.5159457227723684
######################################################################

# Calculating correlation coefficient
correlation_coefficient = np.corrcoef(GPA, GPA_predicted)[0, 1]
print("Correlation Coefficient:", correlation_coefficient)
#Correlation Coefficient: 0.2935382754761457
#given data has positive linear regression
#######################################################################
'''
benefits/impact of the solution :
The solution provides a predictive model to understand the relationship between SAT scores and GPA, 
aiding universities in making informed decisions to enhance academic performance and student success, 
ultimately leading to more personalized and effective educational interventions.
'''









