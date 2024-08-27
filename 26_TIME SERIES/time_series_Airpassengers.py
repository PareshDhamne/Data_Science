# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:08:52 2024

@author: Paresh Dhamne

Problem:
    1.	The dataset consists of monthly totals of international airline passengers from 1995 to 2002. 
    Our main aim is to predict the number of passengers for the next five years using time series forecasting. 
    Prepare a document for each model explaining how many dummy variables you have created and also include the 
    RMSE value for each model.
    
Business Objective:
    maximize:  Increase the accuracy of passenger demand forecasting to optimize resource allocation, 
    improve operational efficiency, and maximize revenue potential for airline companies.
    
    minimize: Minimize the margin of error in passenger demand predictions to avoid overbooking or underutilization of resources, 
    thus reducing costs associated with excess capacity or missed revenue opportunities.

Business Constraits:
    Ensure that the forecasting models consider factors such as seasonality, economic fluctuations, and external events

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.style.use('dark_background')

#load the datset

df=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/TIME SERIES/AirPassengers.csv")
df.columns
df=df.rename({'#Passengers':'Passengers'},axis=1)

print(df.dtypes)
#month is text and passengers in int
#Now let us convert into date and time
df['Month']=pd.to_datetime(df['Month'])
print(df.dtypes)

df.set_index('Month',inplace=True)

plt.plot(df.Passengers)
#thEERE IS INCREASING TREND AND IT HAS GOT SEASONALITY

#Is the data Stationary?
#Dickey-Fuller test
from statsmodels.tsa.stattools import adfuller
adf,pvalue,usedlag_,nobs_,critical_values_,icbest_=adfuller(df)
print("pvalue= ",pvalue,"if aboce 0.05, data is not stationary")

#Since data is not stationary, we may need SARIMA and not just ARIMA
#Now let us extract the year and month from the date and time column

df['year']=[d.year for d in df.index]
df['month']=[d.strftime('%b') for d in df.index]
years=df['year'].unique()


#Plot yearly and monthly values as boxplot
sns.boxplot(x='year',y='Passengers',data=df)

#No.of passengers are going up year by year
sns.boxplot(x='month',y='Passengers',data=df)
#over all there is higher trend in july and August compared to rest of the 

#Extract and plot trend, seasonal and residual
from statsmodels.tsa.seasonal import seasonal_decompose
decomposed=seasonal_decompose(df['Passengers'],model='additive')

#Extract time series:
    #Value=Base Level + trend + Seasonality + Error
    #Multiplicative TIme Series:
        #Value=BAse Level x Trend x Seasonality x Error
        
trend=decomposed.trend
seasonal=decomposed.seasonal
residual=decomposed.resid

plt.figure(figsize=(12,8))
plt.subplot(411)
plt.plot(df['Passengers'],label='Original',color='yellow')
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

#AUTOCORRELATION
#values are not corrleated with x-axis but with its lag
#meanong yeserdays value is depend on day before yesterday so on so forth
#Autocorrelation is simply the correlation of a series with its own lags.
#Plot lag on x axis and correlation on y axis
#Any correlation above confidence lnes are stastically significant.

from statsmodels.tsa.stattools import acf

acf_144=acf(df.Passengers,nlags=144)
plt.plot(acf_144)
#Auto correlation above zero means positive correlation and below as negative correlation
#obatain the same but with single line and more info...
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df.Passengers)
#Any lag before 40 has positive corrleation
#Horizontal bands indicate 95% and 99% (dashed) confidence bands