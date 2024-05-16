# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:31:25 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    Clustering analysis on the telecom dataset segments customers to identify potential churners 
    and factors influencing churn, aiding in minimizing churn, optimizing operational costs, and 
    maximizing revenue from long-term customer relationships while ensuring regulatory compliance.
    

 Business Objective:

Minimize: Risk exposure for insurance companies by identifying high-risk policyholders.

Maximize: Customer satisfaction and retention through personalized insurance offerings.

Business Constraints:  
         Privacy and security of policyholder data.


DATA DICTIONARY:

'Customer': Unique identifier for each customer.
'State': The state where the customer resides.
'Customer Lifetime Value': The predicted net profit attributed to a customer over their entire relationship with the company.
'Response': Whether the customer responded to marketing initiatives.
'Coverage': The type of insurance coverage the customer has.
'Education': The highest level of education attained by the customer.
'Effective To Date': The date when the insurance policy becomes effective.
'EmploymentStatus': The employment status of the customer.
'Gender': The gender of the customer.
'Income': The annual income of the customer.
'Location Code': The type of area where the customer lives (urban, suburban, rural).
'Marital Status': The marital status of the customer.
'Monthly Premium Auto': The monthly premium amount for auto insurance.
'Months Since Last Claim': The number of months since the customer's last insurance claim.
'Months Since Policy Inception': The number of months since the inception of the insurance policy.
'Number of Open Complaints': The number of open complaints registered by the customer.
'Number of Policies': The number of insurance policies held by the customer.
'Policy Type': The type of insurance policy.
'Policy': The specific insurance policy.
'Renew Offer Type': The type of renewal offer provided to the customer.
'Sales Channel': The channel through which the insurance policy was sold.
'Total Claim Amount': The total amount claimed by the customer.
'Vehicle Class': The class of vehicle insured (e.g., SUV, sedan).
'Vehicle Size': The size of the insured vehicle (small, medium, large).
"""
###############################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv("D:/Datasets/AutoInsurance.csv")
df
'''
Out[50]: 
     Customer       State  ...  Vehicle Class Vehicle Size
0     BU79786  Washington  ...   Two-Door Car      Medsize
1     QZ44356     Arizona  ...  Four-Door Car      Medsize
2     AI49188      Nevada  ...   Two-Door Car      Medsize
3     WW63253  California  ...            SUV      Medsize
4     HB64268  Washington  ...  Four-Door Car      Medsize
      ...         ...  ...            ...          ...
9129  LA72316  California  ...  Four-Door Car      Medsize
9130  PK87824  California  ...  Four-Door Car      Medsize
9131  TD14365  California  ...  Four-Door Car      Medsize
9132  UP19263  California  ...  Four-Door Car        Large
9133  Y167826  California  ...   Two-Door Car      Medsize

[9134 rows x 24 columns]
'''
###############################################################################

#EDA
#columns present in dataset
df.columns
'''
Out[51]: 
Index(['Customer', 'State', 'Customer Lifetime Value', 'Response', 'Coverage',
       'Education', 'Effective To Date', 'EmploymentStatus', 'Gender',
       'Income', 'Location Code', 'Marital Status', 'Monthly Premium Auto',
       'Months Since Last Claim', 'Months Since Policy Inception',
       'Number of Open Complaints', 'Number of Policies', 'Policy Type',
       'Policy', 'Renew Offer Type', 'Sales Channel', 'Total Claim Amount',
       'Vehicle Class', 'Vehicle Size'],
      dtype='object')
'''
###############################################################################

df.shape
#Out[52]: (9134, 24)
###############################################################################

#5 number summary
df.describe()
'''
Out[53]: 
       Customer Lifetime Value  ...  Total Claim Amount
count              9134.000000  ...         9134.000000
mean               8004.940475  ...          434.088794
std                6870.967608  ...          290.500092
min                1898.007675  ...            0.099007
25%                3994.251794  ...          272.258244
50%                5780.182197  ...          383.945434
75%                8962.167041  ...          547.514839
max               83325.381190  ...         2893.239678

[8 rows x 8 columns]
'''
###############################################################################

#from this dataset education , customer and policy column is not important drop them
df.drop(['Education','Customer','Policy'],axis=1)

#generate dummy columns
df_new=pd.get_dummies(df)

df_new.columns
'''
Out[56]: 
Index(['Customer Lifetime Value', 'Income', 'Monthly Premium Auto',
       'Months Since Last Claim', 'Months Since Policy Inception',
       'Number of Open Complaints', 'Number of Policies', 'Total Claim Amount',
       'Customer_AA10041', 'Customer_AA11235',
       ...
       'Sales Channel_Web', 'Vehicle Class_Four-Door Car',
       'Vehicle Class_Luxury Car', 'Vehicle Class_Luxury SUV',
       'Vehicle Class_SUV', 'Vehicle Class_Sports Car',
       'Vehicle Class_Two-Door Car', 'Vehicle Size_Large',
       'Vehicle Size_Medsize', 'Vehicle Size_Small'],
      dtype='object', length=9258)
'''
###############################################################################

v=df_new.drop(df_new.loc[:,'Customer_AA10041':],axis=1)

# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normlization function to Univ dataframe gor all the rows
df_norm=norm_fun(v)
df_norm
'''
Out[60]: 
      Customer Lifetime Value    Income  ...  Number of Policies  Total Claim Amount
0                    0.010629  0.562847  ...               0.000            0.132974
1                    0.062406  0.000000  ...               0.875            0.391051
2                    0.134960  0.487763  ...               0.125            0.195764
3                    0.070589  0.000000  ...               0.750            0.183117
4                    0.011245  0.438443  ...               0.000            0.047710
                      ...       ...  ...                 ...                 ...
9129                 0.264137  0.719547  ...               0.125            0.068485
9130                 0.014719  0.216081  ...               0.000            0.131034
9131                 0.076951  0.000000  ...               0.125            0.273297
9132                 0.069098  0.219452  ...               0.250            0.238876
9133                 0.008766  0.000000  ...               0.000            0.127716

[9134 rows x 8 columns]
#it will give us normalize value between 1 to 0
'''
###############################################################################

TWSS=[]
k=list(range(1,10))
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
#Out[64]: array([1, 2, 1, ..., 0, 0, 0])
###############################################################################

mb=pd.Series(model.labels_)

#assign thsi series to df1 dataframe as column and name the column as "cluster
v['clust']=mb

v.head()
'''
Out[67]: 
   Customer Lifetime Value  Income  ...  Total Claim Amount  clust
0              2763.519279   56274  ...          384.811147      1
1              6979.535903       0  ...         1131.464935      2
2             12887.431650   48767  ...          566.472247      1
3              7645.861827       0  ...          529.881344      2
4              2813.692575   43836  ...          138.130879      1

[5 rows x 9 columns]
'''
###############################################################################

v.columns
'''
Out[68]: 
Index(['Customer Lifetime Value', 'Income', 'Monthly Premium Auto',
       'Months Since Last Claim', 'Months Since Policy Inception',
       'Number of Open Complaints', 'Number of Policies', 'Total Claim Amount',
       'clust'],
      dtype='object')
'''
###############################################################################
#assign columns as sequence we want
df=v.iloc[:,:]

df.iloc[:,:].groupby(df.clust).mean()
'''
Out[70]: 
       Customer Lifetime Value  ...  Total Claim Amount
clust                           ...                    
0                  8124.179219  ...          514.900044
1                  8338.440098  ...          329.845572
2                  7117.167580  ...          435.635513

[3 rows x 8 columns]
#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio
'''
###############################################################################

df.to_csv('Kmeans_autoinsurance.csv',encoding='utf-8')
import os
os.getcwd()    
###############################################################################

'''
Benifits to the client:
    In clustering analysis on the telecom dataset, identifying potential churners and factors 
    influencing churn can help minimize churn, optimize operational costs, and maximize revenue 
    from long-term customer relationships, all while ensuring regulatory compliance and customer 
    satisfaction.
'''
###############################################################################






