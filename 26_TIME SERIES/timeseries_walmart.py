# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:14:20 2024

@author: Paresh Dhamne
"""

import pandas as pd
Walmart=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/TIME SERIES/Walmart_Footfalls_Raw.csv")

#pre processing
import numpy as np

Walmart['t']=np.arange(1,160)
Walmart['t_square']=Walmart['t'] * Walmart['t']
Walmart['log_footfalls']=np.log(Walmart['Footfalls'])
Walmart.columns

#month=['jan',feb,mrch,apr,may,jun,july,aug,sep,oct,nov]
#in walmart data we have jan-1991 in 0th column, we need only first
#example- jan from each cell

p=Walmart['Month'][0]
#before we will extract, let us create new column called months to store extracted values
p[0:3]

Walmart['months']=0
#you can check the dataframe with months name with all values 0
#the total reocords are 159 in walmart

for i in range(159):
    p=Walmart['Month'][i]
    Walmart['months'][i]=p[0:3]
    
month_dummies=pd.DataFrame(pd.get_dummies(Walmart['months']))
#now let us concatenate these dummy values to datframe

Walmart1=pd.concat([Walmart,month_dummies],axis=1)
#you can check the dataframe walmart1


#Visualization - Time Plot
Walmart1.Footfalls.plot()

#Data Partition
Train=Walmart1.head(147)
Test=Walmart1.tail(12)

#to change the index value in pandas data frame
#test.set_index(np.arange(1,13))

################## L I N E A R #################################
import statsmodels.formula.api as smf

linear_model=smf.ols('Footfalls ~ t', data=Train).fit()
pred_linear=pd.Series(linear_model.predict(pd.DataFrame(Test['t'])))
remse_linear=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_linear))**2))
remse_linear

########################### Exponential #########################################

Exp =smf.ols('log_footfalls ~ t',data=Train).fit()
pred_Exp=pd.Series(Exp.predict(pd.DataFrame(Test['t'])))
rmse_Exp=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Exp)))**2))
rmse_Exp

################################ Quadritic #######################################

Quad = smf.ols('Footfalls ~ t + t_square',data=Train).fit()
pred_quad=pd.Series(Quad.predict(Test[['t','t_square']]))
rmse_Quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_quad))**2))
rmse_Quad

############################ Additive sesdonality ##################################

add_sea=smf.ols('Footfalls ~ Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_add_sea=pd.Series(add_sea.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]))
rmse_add_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea))**2))
rmse_add_sea

############################# Multiplicative Seasonality ############################

mul_sea=smf.ols('log_footfalls ~ Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_Mult_sea=pd.Series(mul_sea.predict(Test))
rmse_Mult_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mult_sea)))**2))
rmse_Mult_sea

####################### Additive Sesonality Quadritic Trend #####################################################

add_sea_quad=smf.ols('Footfalls ~ t+t_square+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_add_sea_quad=pd.Series(add_sea_quad.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','t','t_square']]))
rmse_add_sea_quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea_quad))**2))
rmse_add_sea_quad

################# Multiplicative Sesonality Linear Trend ##############################

mul_add_sea=smf.ols('log_footfalls ~ t+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_Mult_add_sea=pd.Series(mul_add_sea.predict(Test))
rmse_Mult_add_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mult_add_sea)))**2))
rmse_Mult_add_sea

########################## Testing ################################

data={'Model':pd.Series(['rmse_linear','rmse_Exp','rmse_Quad','rmse_add_sea','rmse_Mult_sea','rmse_add_sea_quad','rmse_Mult_add_sea']),
      "Rmse_Values":pd.Series([remse_linear,rmse_Exp,rmse_Quad,rmse_add_sea,rmse_Mult_sea,rmse_add_sea_quad,rmse_Mult_add_sea])}
table_rmse=pd.DataFrame(data)
table_rmse

#rmse_add_sea has the least value among the models prepared so far

predict_data=pd.read_excel("D:/12-SUPERVISED ALGORTIHM/TIME SERIES/Predict_new.xlsx")

model_full=smf.ols('Footfalls ~ t+t_square+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Walmart1).fit()

pred_new=pd.Series(model_full.predict(predict_data))
pred_new

predict_data['forecasted_Footfalls']=pd.Series(pred_new)

#autoregression Model(AR)
#cslculating Residuals from best model applied on full data
#AV-FV

full_res=Walmart1.Footfalls - model_full.predict(Walmart1)

#ACF plot on residuals
import statsmodels.graphics.tsaplots as tsa_plots
tsa_plots.plot_acf(full_res,lags=12)

#ACF is an (complete) auto- correction function gives values
#of auto- correction of any time series with its lagged values.

#PACF is a partial auro-correction function.
#It finds correlations o present with lags of the residuals of the time series.

tsa_plots.plot_pacf(full_res,lags=12)

#alteranative approch for ACF plot
#from pandas.plotting import autocorrelation_plot
#autocorrelation_ppyplot.show()

#Ar model
from statsmodels.tsa.ar_model import AutoReg
model_ar=AutoReg(full_res, lags=[1])
#model_ar=AutoReg(Train_res,lags=12)
model_fit=model_ar.fit()

print('Coefficients:  %s' % model_fit.params)

pred_res=model_fit.predict(start=len(full_res),end=len(full_res)+len(predict_data)-1,dynamic=False)
pred_res.reset_index(drop=True,inplace=True)

#The final Predictions using ASQT and AR(1) Model
final_pred=pred_new + pred_res
final_pred
