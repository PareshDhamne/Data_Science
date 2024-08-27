# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:16 2024

@author: Hp
"""
import pandas as pd
import statsmodels.graphics.tsaplots as tsa_plots
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot

Walmart=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/TIME SERIES/Walmart_Footfalls_Raw.csv")

#Data partion
Train=Walmart.head(147)
Test=Walmart.tail(12)

#in order to use this model, we need to first find out values p,q,and d
#p represents number of Autoregressive terms - lag of dependent variable.
#q represents number of moving averages terms - lagged forecast errors in prediction equation.
# d represents number of non-seasonl differences.
#To find the values of p,d,q-we use Autocorrelation function (ACF)
#and partial Autocorrelation (PACF) plots.
#p value is the value on x-axis of PACF where the plot crosses
#the upper Confidence Interval for the firt time

tsa_plots.plot_acf(Walmart.Footfalls,lags=12)
#q for MA 5 

tsa_plots.plot_pacf(Walmart.Footfalls,lags=12)
#p for AR


#ARIMA with AR=3 , MA=5

model1=ARIMA(Train.Footfalls, order=(3,1,5))
res1=model1.fit()
print(res1.summary())

#Forecast for next 12 months
start_index=len(Train)
end_index=start_index + 11
Forecast_test=res1.predict(start=start_index,end=end_index)
print(Forecast_test)

#Evalute forests
rmse_test=sqrt(mean_squared_error(Test.Footfalls,Forecast_test))
print('Test RMSE:%.3f' % rmse_test)

#plot forecasts against actual outcomes
pyplot.plot(Test.Footfalls)
pyplot.plot(Forecast_test,color='red')
pyplot.show()

#AUTO-ARIMA- Automatically discover the optimal order for an ARIMA
#pip install pmdarima --user

import pmdarima as pm

ar_modelpm.auto_arima(Train.Footfalls,start_p=0,start_q=0,max_p=12,max_q=12,#maximam p and q,m=1#frequence )