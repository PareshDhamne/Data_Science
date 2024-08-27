# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:07:58 2024

@author: Paresh Dhamne

Problem:
    Solar power consumption has been recorded by city councils at regular intervals. 
    The reason behind doing so is to understand how businesses are using solar power 
    so that they can cut down on nonrenewable sources of energy and shift towards renewable energy. 
    Based on the data, build a forecasting model and provide insights on it. 
    
Business Objective:
    Maximize: Increase the utilization of solar power by businesses to reduce reliance on nonrenewable energy sources, 
    thereby maximizing environmental sustainability and cost savings.
    
    Minimize: Minimize the carbon footprint and environmental impact of businesses
    by promoting the adoption of solar power as a primary energy source, reducing dependence on 
    fossil fuels and mitigating climate change risks.
    
Business Constraints:
    Ensure that the existing infrastructure can support the adoption of solar power, 
    considering factors such as available roof space, grid connectivity, and regulatory constraints.
    
Data Dictionary:
    date: Represents the timestamp for solar power consumption data collection, providing temporal context for analysis.
    cum_power: Indicates the cumulative amount of solar power consumed up to the corresponding date, 
    essential for assessing overall energy usage trends.
    
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.style.use('dark_background')
##########################################################################################
#load the datset

df=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/TIME SERIES/Datasets_Forecasting(1)/solarpower_cumuldaybyday2.csv")
df.columns

#########################################################################################

print(df.dtypes)
'''
date          object
cum_power    float64
dtype: object
'''
##################################################################################

df.describe()
'''
Out[32]: 
         cum_power
count   2558.000000
mean   13461.057349
std     8129.192104
min        0.100000
25%     6665.350000
50%    13000.500000
75%    20183.750000
max    28120.000000
'''
#################################################################################

#month is text and Sales in int
#Now let us convert into date and time
df['date']=pd.to_datetime(df['date'])
print(df.dtypes)

df.set_index('date',inplace=True)
###################################################################################
plt.plot(df.cum_power)
#thEERE IS INCREASING TREND AND IT HAS GOT SEASONALITY
#################################################################################
#Is the data Stationary?
#Dickey-Fuller test
from statsmodels.tsa.stattools import adfuller
adf,pvalue,usedlag_,nobs_,critical_values_,icbest_=adfuller(df)
print("pvalue= ",pvalue,"if above 0.05, data is not stationary")
#pvalue=  0.9064494730945615 if above 0.05, data is not stationary
#Since data is not stationary, we may need SARIMA and not just ARIMA
#Now let us extract the year and month from the date and time column

df['year']=[d.year for d in df.index]
df['month']=[d.strftime('%b') for d in df.index]
years=df['year'].unique()


#Plot yearly and monthly values as boxplot
sns.boxplot(x='year',y='cum_power',data=df)
#No.of passengers are going up year by year

sns.boxplot(x='month',y='cum_power',data=df)
#over all there is higher trend in oct compared to rest of the other month.
###################################################################################

#Extract and plot trend, seasonal and residual
from statsmodels.tsa.seasonal import seasonal_decompose
decomposed=seasonal_decompose(df['cum_power'],model='additive')

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
plt.plot(df['cum_power'],label='Original',color='yellow')
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

acf_144=acf(df.cum_power,nlags=144)
plt.plot(acf_144)
#Auto correlation above zero means positive correlation and below as negative correlation
#obatain the same but with single line and more info...
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df.cum_power)
#Any lag before 40 has positive corrleation
#Horizontal bands indicate 95% and 99% (dashed) confidence bands
#####################################################################

# Forecasting using SARIMA model
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from math import sqrt

# Splitting data into train and test sets
train = df[:'2023-12-31']
test = df['2024']

# Fit SARIMA model
sarima_model = SARIMAX(train['cum_power'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_result = sarima_model.fit()

# Forecast solar power consumption for the next year
forecast = sarima_result.forecast(steps=len(test))

# Calculate RMSE
rmse = sqrt(mean_squared_error(test, forecast))
print("RMSE:", rmse)

# Plot actual vs forecasted solar power consumption
plt.figure(figsize=(12, 6))
plt.plot(train.index, train['cum_power'], label='Train', color='yellow')
plt.plot(test.index, test['cum_power'], label='Test', color='green')
plt.plot(test.index, forecast, label='Forecast', color='red')
plt.title('Actual vs Forecasted Solar Power Consumption')
plt.xlabel('Date')
plt.ylabel('Cumulative Power (kWh)')
plt.legend()
plt.show()
###################################################################
'''
The solution enables city councils to strategically allocate resources and promote solar energy adoption, 
fostering environmental sustainability and cost savings while complying with regulatory 
standards and enhancing community engagement.
'''
