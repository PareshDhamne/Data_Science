# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:49:21 2024

@author: Paresh Dhamne
Problem:
    A logistics company recorded the time taken for delivery and the time taken for the sorting of the items for delivery. 
    Build a Simple Linear Regression model to find the relationship between delivery time and sorting time with delivery time 
    as the target variable. Apply necessary transformations and record the RMSE and correlation coefficient values for different models.
    
Business Objective:
    
    Minimize: Minimizing discrepancies between predicted and actual delivery times to ensure timely deliveries, 
              reducing operational costs associated with delays
              
    Maximize: Optimizing sorting efficiency to minimize delivery time, 
              thereby enhancing customer satisfaction and loyalty through faster delivery services.
    
Business Constraints:
    Ensure that the model's predictions are based on ethical data practices, 
    maintaining confidentiality and privacy of customer information and delivery data.
    
DATA DICTIONARY:
    Delivery Time: Column records the duration for delivery of items numrical data
    Sorting Time: column records the duration spent on sorting items before delivery numerical data
"""


import pandas as pd 
import numpy as np 
import seaborn as sns
from sklearn import linear_model 
import matplotlib.pyplot as plt

data=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Regression/Datasets_SLR(1)/delivery_time.csv")
data
##################################################################

#Rename the column name
data.columns=data.columns.str.replace(' ', '_')
data.columns
#Out[15]: Index(['Delivery_Time', 'Sorting_Time'], dtype='object')
###################################################################

data.shape
#Out[16]: (21, 2)
##############################################################
data.size
#Out[11]: 42
################################################################
data.dtypes
'''
Out[22]: 
Delivery_Time    float64
Sorting_Time       int64
dtype: object
'''
#############################################################
data.sum().isnull()
'''
data.sum().isnull()
Out[18]: 
Delivery_Time    False
Sorting_Time     False
dtype: bool

There is no null value in given data
'''
#########################################################################
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21 entries, 0 to 20
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Delivery_Time  21 non-null     float64
 1   Sorting_Time   21 non-null     int64  
dtypes: float64(1), int64(1)
memory usage: 468.0 bytes
'''
#########################################################################
data.describe()
'''
Out[19]: 
       Delivery_Time  Sorting_Time
count      21.000000     21.000000
mean       16.790952      6.190476
std         5.074901      2.542028
min         8.000000      2.000000
25%        13.500000      4.000000
50%        17.830000      6.000000
75%        19.750000      8.000000
max        29.000000     10.000000
#it will provide 5 number summary of dataset
'''
#########################################################################

#Boxplot
sns.boxplot(x=data["Delivery_Time"])
sns.boxplot(x=data["Sorting_Time"])
#there are no outliers are present in given data
#########################################################

#Draw scatter plot 
plt.xlabel('Delivery_Time)')
plt.ylabel('Sorting_Time')
plt.scatter(data['Delivery_Time'],data['Sorting_Time'],color='red',marker='+')
#most of the delivery time is between 15 to 20 and sorting time between 5 to 8
#######################################################################

#get target variable
new_df=data.drop('Delivery_Time',axis='columns')
new_df

delivery_time=data['Delivery_Time']
delivery_time

##################################################################3
#create linear regression model
reg= linear_model.LinearRegression()
reg.fit(new_df,delivery_time)

#predict calories used for weight gained
reg.predict([[10]])
#Out[35]: array([23.07293294])

#coefficeint of regression
reg.coef_
#Out[36]: array([1.6490199])

reg.intercept_
#Out[37]: 6.58273397199706

#Equation of simple regular expression
#y=m*X+b

y=10*reg.intercept_+reg.coef_
y
#Out[39]: array([67.47635962])
#########################################################################
# 30
reg.predict([[30]])
#########################################################################

from sklearn.metrics import mean_squared_error, r2_score

# Predict delivery time based on sorting time
delivery_time_predicted = reg.predict(new_df)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(delivery_time, delivery_time_predicted))
print("Root Mean Squared Error (RMSE):", rmse)
#Root Mean Squared Error (RMSE): 2.7916503270617654
# the difference between the actual calories consumed and the predicted calories
# consumed by the model is approximately 2.7916503270617654
######################################################################

# Calculating correlation coefficient
correlation_coefficient = np.corrcoef(delivery_time, delivery_time_predicted)[0, 1]
print("Correlation Coefficient:", correlation_coefficient)
#Correlation Coefficient: 0.8259972607955325
#given data has  positive linear regression
#######################################################################
'''
benefits/impact of the solution :
The solution optimizes delivery operations, ensuring timely deliveries, cost reduction, 
and enhanced customer satisfaction, thereby providing the logistics company 
with a competitive edge and improved profitability.
'''






