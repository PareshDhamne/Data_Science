# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:53:23 2023

@author: Lenovo
"""

import pandas as pd
df=pd.read_csv('Computer_data.csv')
df
df.dtypes
df2=df.convert_dtypes()
df2.dtypes
######
df3=df.astype(str)
df3.dtypes
############
df.columns
df3=df.rename({'price':'PRICE','speed':'SPEED'},axis=1)
df3
#################
cols=['speed','hd','ram','cd']
df4=df[cols].astype(str)
df4
#####################
df5=df.astype({'speed':'float'},errors='ignore')
df5
###################
df6=df.astype({'speed':'float'},errors='raised')
df6
####################
df.columns
df.columns.values
df.index
df.dtypes
#################
df['speed']
#################
df[['speed','hd']]
################
df7=df.drop([1,3])
df7
##############
df8=df.drop(df.index[[2,4]])
df8
##############
df8=df.drop(df.index[2:])
df8
#################
df9=df.drop(['hd'],axis=1)
df9
###############
df.drop(df.columns[[2]],axis=1,inplace=True)
df
##############
import pandas as pd
import numpy as np
df.columns
df.loc[:,'hd':]
###############
import random
row_label=['r0','r1','r2','r3','r4','r5']
df8=pd.DataFrame(df,[random.choice(row_label) for i in range(405)])
df8
##############
#different ways to access row by index
df.iloc[2]             #select 2nd row
df.iloc[1:3]            #select first three rows
df.iloc[-1:]            #select last row
df.iloc[[2,3,4]]        #select particular row
df.iloc[:0]             #empty row
df.iloc[:1]             #slect first row
df.iloc[-3:]            #select last three row
df.iloc[::2]    
####################
df8.loc['r1']
df8.loc[['r1','r2','r3']]
###################
df.dtypes
df9=df.query('hd==80')
df9
#################3
df9=df.query('hd!=80')
df9
################3

















