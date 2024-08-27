# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:39:22 2024

@author: Paresh Dhamne

Problem:
    A plastics manufacturing plant has recorded their monthly sales data from 1949 to 1953. 
    Perform forecasting on the data and bring out insights from it and forecast the sale for the next year. 

Business Objective:
    Maximize: Increase sales revenue through effective resource allocation and targeted marketing strategies.
    
    Minimize: Reduce inventory costs by accurately forecasting demand and optimizing production schedules.

Business Constaints:
    Ensure that sales forecasts align with the plant's production capacity to 
    avoid bottlenecks and maintain operational efficiency.
    
Data Dictionary:
    Month: Represents the categorical variable denoting the month of sales data collection, 
    providing temporal context for analysis.
    Sales: Numerical variable indicating the quantity of products sold in each corresponding month, 
    essential for assessing revenue trends and forecasting future sales.

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.style.use('dark_background')
##########################################################################################
#load the datset

df=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/TIME SERIES/Datasets_Forecasting(1)/PlasticSales.csv")
df.columns

#########################################################################################

print(df.dtypes)
'''
Month    object
Sales     int64
dtype: object
'''
##################################################################################

df.describe()
'''
Out[32]: 
             Sales         year
count    60.000000    60.000000
mean   1162.366667  2051.000000
std     266.431469     1.426148
min     697.000000  2049.000000
25%     947.750000  2050.000000
50%    1148.000000  2051.000000
75%    1362.500000  2052.000000
max    1637.000000  2053.000000
'''
#################################################################################

#month is text and Sales in int
#Now let us convert into date and time
df['Month']=pd.to_datetime(df['Month'])
print(df.dtypes)

df.set_index('Month',inplace=True)
###################################################################################
plt.plot(df.Sales)
#thEERE IS INCREASING TREND AND IT HAS GOT SEASONALITY
#################################################################################
#Is the data Stationary?
#Dickey-Fuller test
from statsmodels.tsa.stattools import adfuller
adf,pvalue,usedlag_,nobs_,critical_values_,icbest_=adfuller(df)
print("pvalue= ",pvalue,"if above 0.05, data is not stationary")
#pvalue=  0.8354143931554413 if above 0.05, data is not stationary
#Since data is not stationary, we may need SARIMA and not just ARIMA
#Now let us extract the year and month from the date and time column

df['year']=[d.year for d in df.index]
df['month']=[d.strftime('%b') for d in df.index]
years=df['year'].unique()


#Plot yearly and monthly values as boxplot
sns.boxplot(x='year',y='Sales',data=df)
#No.of passengers are going up year by year

sns.boxplot(x='month',y='Sales',data=df)
#over all there is higher trend in july and August compared to rest of the other month.
###################################################################################

#Extract and plot trend, seasonal and residual
from statsmodels.tsa.seasonal import seasonal_decompose
decomposed=seasonal_decompose(df['Sales'],model='additive')

#Extract time series:
    #Value=Base Level + trend + Seasonality + Error
    #Multiplicative TIme Series:
        #Value=BAse Level x Trend x Seasonality x Error
############################################################################

trend=decomposed.trend
seasonal=decomposed.seasonal
residual=decomposed.resid

plt.figure(figsize=(12,8))
plt.subplot(411)
plt.plot(df['Sales'],label='Original',color='yellow')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend,label="Trend",color='yellow')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal,label='Seasonal',color='yellow')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual,label='Residual',color='yellow')
plt.legend(loc='upper left')
plt.show()

'''
Trend is going up from 1950s to 60s
It is highly seasonal showing peaks at particular interval
This helps to select specific prediction model
'''
###########################################################################

#AUTOCORRELATION
#values are not corrleated with x-axis but with its lag
#meanong yeserdays value is depend on day before yesterday so on so forth
#Autocorrelation is simply the correlation of a series with its own lags.
#Plot lag on x axis and correlation on y axis
#Any correlation above confidence lnes are stastically significant.

from statsmodels.tsa.stattools import acf

acf_144=acf(df.Sales,nlags=144)
plt.plot(acf_144)
#Auto correlation above zero means positive correlation and below as negative correlation
#obatain the same but with single line and more info...
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df.Sales)
#Any lag before 40 has positive corrleation
#Horizontal bands indicate 95% and 99% (dashed) confidence bands
##############################################################################

'''
The business benefits from improved sales forecasting accuracy, 
allowing for more effective resource allocation and inventory management, 
ultimately leading to higher revenue and lower operational costs. 
'''