# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:18:19 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    Perform clustering analysis on the telecom dataset. The data is a mixture of both categorical 
    and numerical data. It consists of the number of customers who churn. Derive insights and get 
    possible information on factors that may affect the churn decision. 
    Refer to Telco_customer_churn.xlsx dataset.

Business Objective:

Minimize: Operational costs associated with acquiring new customers to replace churned ones.

Maximize: Revenue from long-term customer relationships and increased customer lifetime value.

Business Constraints:  
     Data quality and availability for analysis, especially regarding historical churn data.
     

DATA DICTIONARY:
    '''
    The data is a mixture of both categorical and numerical data.
    It consists of the number of customers who churn out.
    Derive insights and get possible information on factors that
    may affect the churn decision. Refer to Telco_customer_churn.xlsx dataset.
    This sample data module tracks a fictional telco company's customer churn based 
    on various factors.T he churn column indicates whether the customer
    departed within the last month. 
    Other columns include gender, dependents, monthly charges,
    and many with information about the types 
    of services each customer has.
"""
###############################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_excel("D:/Datasets/Telco_customer_churn.xlsx")
df
'''
Out[26]: 
     Customer ID  Count  ... Total Long Distance Charges Total Revenue
0     8779-QRDMV      1  ...                        0.00         59.65
1     7495-OOKFY      1  ...                      390.80       1024.10
2     1658-BYGOY      1  ...                      203.94       1910.88
3     4598-XLKNJ      1  ...                      494.00       2995.07
4     4846-WHAFZ      1  ...                      234.21       3102.36
         ...    ...  ...                         ...           ...
7038  2569-WGERO      1  ...                     1639.44       3039.53
7039  6840-RESVB      1  ...                      865.20       2807.47
7040  2234-XADUH      1  ...                     2135.52       9453.04
7041  4801-JZAZL      1  ...                        0.00        319.21
7042  3186-AJIEK      1  ...                     2043.36       8887.86

[7043 rows x 30 columns]
'''
###############################################################################

#EDA
#columns present in dataset
df.columns
'''
Out[27]: 
Index(['Customer ID', 'Count', 'Quarter', 'Referred a Friend',
       'Number of Referrals', 'Tenure in Months', 'Offer', 'Phone Service',
       'Avg Monthly Long Distance Charges', 'Multiple Lines',
       'Internet Service', 'Internet Type', 'Avg Monthly GB Download',
       'Online Security', 'Online Backup', 'Device Protection Plan',
       'Premium Tech Support', 'Streaming TV', 'Streaming Movies',
       'Streaming Music', 'Unlimited Data', 'Contract', 'Paperless Billing',
       'Payment Method', 'Monthly Charge', 'Total Charges', 'Total Refunds',
       'Total Extra Data Charges', 'Total Long Distance Charges',
       'Total Revenue'],
      dtype='object')
'''
###############################################################################

#display number of rows and columns
df.shape
#Out[28]: (7043, 30)
###############################################################################

#check any null values is there in dataset
df.isnull().sum()
'''
Out[30]: 
Customer ID                          0
Count                                0
Quarter                              0
Referred a Friend                    0
Number of Referrals                  0
Tenure in Months                     0
Offer                                0
Phone Service                        0
Avg Monthly Long Distance Charges    0
Multiple Lines                       0
Internet Service                     0
Internet Type                        0
Avg Monthly GB Download              0
Online Security                      0
Online Backup                        0
Device Protection Plan               0
Premium Tech Support                 0
Streaming TV                         0
Streaming Movies                     0
Streaming Music                      0
Unlimited Data                       0
Contract                             0
Paperless Billing                    0
Payment Method                       0
Monthly Charge                       0
Total Charges                        0
Total Refunds                        0
Total Extra Data Charges             0
Total Long Distance Charges          0
Total Revenue                        0
dtype: int64
'''
###############################################################################

#5 number summary
df.describe()
'''
Out[31]: 
        Count  Number of Referrals  ...  Total Long Distance Charges  Total Revenue
count  7043.0          7043.000000  ...                  7043.000000    7043.000000
mean      1.0             1.951867  ...                   749.099262    3034.379056
std       0.0             3.001199  ...                   846.660055    2865.204542
min       1.0             0.000000  ...                     0.000000      21.360000
25%       1.0             0.000000  ...                    70.545000     605.610000
50%       1.0             0.000000  ...                   401.440000    2108.640000
75%       1.0             3.000000  ...                  1191.100000    4801.145000
max       1.0            11.000000  ...                  3564.720000   11979.340000

[8 rows x 11 columns]
'''
###############################################################################

# we are checking which column is not necserray or
# the column which is  numerical data  that can be place in the datframe
df1=df.drop(['Customer ID','Count', 'Quarter', 'Referred a Friend', 'Offer', 'Phone Service',
       'Multiple Lines','Internet Service', 'Internet Type', 'Online Security', 
       'Online Backup', 'Device Protection Plan','Premium Tech Support', 'Streaming TV',
       'Streaming Movies','Streaming Music', 'Unlimited Data', 'Contract',
       'Paperless Billing','Payment Method'],axis=1) 

df1.columns
'''
Out[33]: 
Index(['Number of Referrals', 'Tenure in Months',
       'Avg Monthly Long Distance Charges', 'Avg Monthly GB Download',
       'Monthly Charge', 'Total Charges', 'Total Refunds',
       'Total Extra Data Charges', 'Total Long Distance Charges',
       'Total Revenue'],
      dtype='object')
'''
###############################################################################

df1.shape
#Out[34]: (7043, 10)
###############################################################################

# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normlization function to Univ dataframe gor all the rows
df_norm=norm_fun(df1.iloc[:,:])
#it will give us normalize value between 1 to 0

TWSS=[]
k=list(range(1,6))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
TWSS
#as k value increases the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters");
plt.ylabel("Total_within_SS");
#shows elbow graph for given dataset
###############################################################################

model=KMeans(n_clusters=3)

model.fit(df_norm)

model.labels_
#Out[40]: array([0, 0, 0, ..., 1, 0, 1])
###############################################################################

mb=pd.Series(model.labels_)

#assign thsi series to df1 dataframe as column
df1['clust']=mb

df=df1.iloc[:,[10,1,2,3,4,5,6,7,8,9]]

df.iloc[:,:].groupby(df.clust).mean()
'''
Out[44]: 
       Tenure in Months  ...  Total Revenue
clust                    ...               
0             11.413997  ...     986.708924
1             57.365949  ...    6897.832319
2             48.739070  ...    2610.167994

[3 rows x 9 columns]
'''
#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio
###############################################################################

df.to_csv('Kmeans_telco_churn_case.csv',encoding='utf-8')
import os
os.getcwd()    
###############################################################################

'''
Benifits to the client:
    Clustering analysis on the telecom dataset segments customers to identify potential churners 
    and factors influencing churn, aiding in minimizing churn, optimizing operational costs, and 
    maximizing revenue from long-term customer relationships while ensuring regulatory compliance.
'''
###############################################################################