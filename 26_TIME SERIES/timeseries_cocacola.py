# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:08:29 2024

@author: Paresh Dhamne

Problem:
    2.	The dataset consists of quarterly sales data of Coca-Cola from 1986 to 1996.
    Predict sales for the next two years by using time series forecasting and prepare a document for each model explaining how many dummy 
    variables you have created and also include the RMSE value for each model.
    
Business Objective:
    Maximize: Improve the accuracy of sales forecasts to optimize inventory management, 
    production planning, and marketing strategies, thereby maximizing revenue and profitability for Coca-Cola.
    
    Minimize: Minimize the margin of error in sales predictions to avoid stockouts or overstock situations,
    reducing costs associated with excess inventory holding or missed sales opportunities.
    
Business Constraits:
    Ensure that the forecasting models consider various factors such as seasonality, 
    consumer trends, market competition, and economic conditions, to provide reliable sales predictions 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import Holt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

#now to load the dataset

cocacola=pd.read_excel("D:/12-SUPERVISED ALGORTIHM/TIME SERIES/CocaCola_Sales_Rawdata.xlsx")

#let us plot the dataset and its nature
cocacola.Sales.plot()

#splitting the data into train and test set data
#since we are working on quartely datasets and in year there are
#test data=4 quarters
#train data = 38
Train=cocacola.head(38)
Test=cocacola.tail(4)
#here we are onsidering performance parameters as mean absolute percentage error
#rathet=r than mean sqauare error
#custom function is written to calculate MPSE
def MAPE(pred,org):
    temp=np.abs((pred-org)/org)*100
    return np.mean(temp)

#EDA which comprises identification of level, trends ans seasonal
#In order to seperate Trend and Seasoality moving average can
my_pred=cocacola['Sales'].rolling(4).mean()
my_pred.tail(4)
#now let us calculate mean absolute percentage of these valuse
MAPE(my_pred.tail(4),Test.Sales)
#moving average is predicting complete values, out of which last  
#are considered as predicted values and last four values of test
#basic purpose of moving average is deseasonalizing
cocacola.Sales.plot(label='org')
#This is original plot
#now let us seperate out Trend and Seasonality
for i in range(2,9,2):
    #it will take windowsize 2,4,6,8
    cocacola['Sales'].rolling(i).mean().plot(label=str(i))
    plt.legend(loc=3)
#you can see i=4 and 8 are deseasonable plots

#Time series decomposition is the another technique od seperating seasonality
decompose_ts_add=seasonal_decompose(cocacola.Sales,model='additive',period=4)

print(decompose_ts_add.trend)
print(decompose_ts_add.seasonal)
print(decompose_ts_add.resid)
print(decompose_ts_add.observed)
decompose_ts_add.plot()

#similar plot can be decomposed using multiplicative
decompose_ts_mul=seasonal_decompose(cocacola.Sales,model='multiplicaitve',period=4)
print(decompose_ts_mul.trend)
print(decompose_ts_mul.seasonal)
print(decompose_ts_mul.resid)
print(decompose_ts_mul.observed)
decompose_ts_mul.plot()
#you can obsrved the difference between these plots
#Now let us plot ACF plot to check the auto correlation
import statsmodels.graphics.tsaplots as tsa_plots
tsa_plots.plot_acf(cocacola.Sales,lags=4)
#we can observe the output in which r1,r2,r3 and r4 has higher
##This is all about EDA
#Let us apply data to data driven models
#simple exponential method
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
ses_model=SimpleExpSmoothing(Train['Sales']).fit()
pred_ses=ses_model.predict(start=Test.index[0],end=Test.index[-1])

#now calculate MAPE
MAPE(pred_ses,Test.Sales)
#we are getting8.307897760532047
#Holts exponential smoothing 
#here only trend is captured
hw_model=Holt(Train['Sales']).fit()
pred_hw=hw_model.predict(start=Test.index[0],end=Test.index[-1])
MAPE(pred_hw,Test.Sales)
#9.80978335866318

#Holts winter exponential smoothing with additive sesonality
hwe_model_add_add=ExponentialSmoothing(Train['Sales'],seasonal='add',trend='add',seasonal_periods=4).fit()
pred_hwe_model_add_add=hwe_model_add_add.predict(start=Test.index[0],end=Test.index[-1])
MAPE(pred_hwe_model_add_add,Test.Sales)
#seasonal='add',trend='add',seasonal_periods=4).fit()

#Holts winter exponential smoothing with multiplicative seasona
hwe_model_mul_add=ExponentialSmoothing(Train['Sales'],seasonal='mul',trend='add',seasonal_periods=4).fit()
pred_hwe_model_mul_add=hwe_model_mul_add.predict(start=Test.index[0],end=Test.index[-1])
MAPE(pred_hwe_model_add_add,Test.Sales)
#Out[52]: 3.372576621498227


















MAPE(newdata_pred,Test.Sales)
newdata_pred