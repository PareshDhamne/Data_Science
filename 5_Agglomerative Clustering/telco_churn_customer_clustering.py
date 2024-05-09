# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:41:40 2023

@author: PARESH DHAMNE

Problem statement:
    Perform clustering analysis on the telecom data set.The data is a mixture of both categorical 
    and numerical data. It consists of the number of customers who churn out. Derive insights and 
    get possible information on factors that may affect the churn decision. 
    Refer to Telco_customer_churn.xlsx dataset.

Business Objective:

Minimize: Operational costs associated with acquiring new customers to replace churned ones.

Maximize: Revenue from long-term customer relationships and increased customer lifetime value.

Business Constraints:  
     Data quality and availability for analysis, especially regarding historical churn data.


DATA DICTIONARY:
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
#####################################################################

import pandas as pd
import matplotlib.pyplot as plt

#now import file from data sett and create a dataframe
df=pd.read_excel("D:/Datasets/Telco_customer_churn.xlsx")

df.describe()
'''
Out[24]: 
        Count  Number of Referrals  ...  Total Long Distance Charges  Total Revenue
count  7043.0          7043.000000  ...                  7043.000000    7043.000000
mean      1.0             1.951867  ...                   749.099262    3034.379056
std       0.0             3.001199  ...                   846.660055    2865.204542
min       1.0             0.000000  ...                     0.000000      21.360000
25%       1.0             0.000000  ...                    70.545000     605.610000
50%       1.0             0.000000  ...                   401.440000    2108.640000
75%       1.0             3.000000  ...                  1191.100000    4801.145000
max       1.0            11.000000  ...                  3564.720000   11979.340000
'''
#######################################################################

df.shape
#Out[25]: (7043, 30)
#######################################################################

df.columns
'''
Out[26]: 
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
########################################################################

#we have one column 'award' which really not useful we will drop it
df1=df.drop(['Customer ID','Count', 'Quarter', 'Referred a Friend', 'Offer', 'Phone Service','Multiple Lines','Internet Service', 'Internet Type', 'Online Security', 
       'Online Backup', 'Device Protection Plan','Premium Tech Support', 'Streaming TV','Streaming Movies','Streaming Music', 'Unlimited Data', 'Contract',
       'Paperless Billing','Payment Method'],axis=1)
###########################################################################

#display number of rows and columns
df.shape
#Out[28]: (7043, 30)
###################################################################

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
#################################################################

df1.head(15)

df1.columns

df1.dtypes
'''
Out[33]: 
Number of Referrals                    int64
Tenure in Months                       int64
Avg Monthly Long Distance Charges    float64
Avg Monthly GB Download                int64
Monthly Charge                       float64
Total Charges                        float64
Total Refunds                        float64
Total Extra Data Charges               int64
Total Long Distance Charges          float64
Total Revenue                        float64
dtype: object
'''
#####################################################################

#we know that there is scale difference among the columns, which we have to remove
#either by using normalization or standardization
#whenever there is mixed data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normalization function to df1 dataframe  rows
df_norm=norm_func(df1.iloc[:,:])
df_norm
'''
Out[36]: 
      Number of Referrals  ...  Total Revenue
0                0.000000  ...       0.003202
1                0.090909  ...       0.083855
2                0.000000  ...       0.158013
3                0.090909  ...       0.248680
4                0.090909  ...       0.257652
                  ...  ...            ...
7038             0.000000  ...       0.252398
7039             0.090909  ...       0.232992
7040             0.363636  ...       0.788735
7041             0.090909  ...       0.024908
7042             0.000000  ...       0.741471

[7043 rows x 10 columns]
'''
################################################################

#you can check the df_norm dataframe which is scaled between values from 0 to 1
#you can apply describe function to new dataframe
b=df_norm.describe()
b
'''
Out[38]: 
       Number of Referrals  ...  Total Revenue
count          7043.000000  ...    7043.000000
mean              0.177442  ...       0.251967
std               0.272836  ...       0.239606
min               0.000000  ...       0.000000
25%               0.000000  ...       0.048859
50%               0.000000  ...       0.174551
75%               0.272727  ...       0.399715
max               1.000000  ...       1.000000

[8 rows x 10 columns]
'''
##################################################################

# plot dendrogram first
#now to create dendrogram we need to measure distance,

#we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

#linkage function  gives us hirerarchicsl or algorithmic clustering
#ref the help for linkage
z=linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8));
plt.title("Hirerchical Clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#applying agglomerative clustering choosing 3 as clusetrs from dendrogram

###################################################################
from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)
#apply labels to the clusters

h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)

#assign thsi series to univ dataframe as column and name the column as "cluster
df1['clust']=cluster_labels

df=df1.iloc[:,[10,1,2,3,4,5,6,7,8,9]]

df.iloc[:,:].groupby(df.clust).mean()
'''
Out[22]: 
       Tenure in Months  ...  Total Revenue
clust                    ...               
0             52.544597  ...    4959.500519
1             63.644845  ...    8229.791358
2             16.263171  ...    1165.164380

[3 rows x 9 columns]
'''
#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio
########################################################################

df.to_csv("teledata.csv",encoding='utf-8')
import os
os.getcwd()
#######################################################################

'''
Benifit to the client:
    The clustering analysis on telecom data identifies customer segments based on 
    churn factors, enabling targeted retention strategies and resource allocation, 
    thus minimizing operational costs and maximizing revenue from long-term customer relationships.
'''
######################################################################