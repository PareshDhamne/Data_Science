# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:10:19 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    Analyze the information given in the following ‘Insurance Policy dataset’ to            
    create clusters of persons falling in the same type. Refer to Insurance Dataset.csv
    

Business Objective:

    Maximize: Increase customer satisfaction and policy retention by identifying and addressing 
    specific needs and preferences of different customer segments.
    
    Minimize: Reduce policy churn and attrition rates by proactively addressing customer dissatisfaction
    
Business Constraints:
    Ensure compliance with legal and regulatory requirements governing the insurance industry, 
    including data privacy laws, insurance regulations, and consumer protection laws.
    
    '''
    DATA DICTIONARY:
        
    Premiums Paid: Amount paid by customers as insurance premiums.
    Age: Customer's age, a demographic factor.
    Days to Renew: Remaining days until insurance policy renewal.
    Claims made: Number of insurance claims filed by customers.
    Income: Customer's income level, a socioeconomic factor.
"""
###############################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv("D:/Datasets/Insurance Dataset.csv")
df
'''
Out[6]: 
    Premiums Paid  Age  Days to Renew   Claims made  Income
0            2800   26            233   3890.076336   28000
1            2950   27            130   2294.444444   29500
2            3100   28            144   2564.545455   31000
3            3250   30             65   1978.260870   32500
4            3400   32             56   2009.090909   34000
..            ...  ...            ...           ...     ...
95          25575   63             76  16161.979170  170500
96          25800   62            166  23715.151520  172000
97          26025   59            167  24043.401020  173500
98          26250   58            245  40147.058820  175000
99          26475   52            261  46781.067960  176500

[100 rows x 5 columns]
'''
###############################################################################

#EDA
#columns present in dataset
df.columns
# Index(['Premiums Paid', 'Age', 'Days to Renew', 'Claims made', 'Income'], dtype='object')
###############################################################################

#display number of rows and columns
df.shape
#Out[7]: (100, 5)
###############################################################################

#check any null values is there in dataset
df.isnull().sum()
'''
Out[8]: 
Premiums Paid    0
Age              0
Days to Renew    0
Claims made      0
Income           0
dtype: int64
'''
###############################################################################

#5 number summary
df.describe()
'''
Out[9]: 
       Premiums Paid         Age  Days to Renew   Claims made         Income
count     100.000000  100.000000     100.000000    100.000000     100.000000
mean    12542.250000   46.110000     120.400000  12578.993367  102250.000000
std      6790.731666   13.887641      88.055767  13695.906762   43517.237964
min      2800.000000   23.000000       1.000000   1978.260870   28000.000000
25%      6975.000000   34.000000      56.000000   5220.648735   65125.000000
50%     11825.000000   45.000000      89.000000   8386.043907  102250.000000
75%     15475.000000   54.500000     186.500000  14670.889520  139375.000000
max     29900.000000   82.000000     321.000000  99676.744190  176500.000000
'''
#except 1st all columns are important so we are not dropping any column
###############################################################################

# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normlization function to Univ dataframe gor all the rows
df_norm=norm_fun(df.iloc[:,:])
#it will give us normalize value between 1 to 0
###############################################################################

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
'''
Out[15]: 
array([2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1,
       1, 2, 0, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
'''
###############################################################################
mb=pd.Series(model.labels_)

#assign thsi series to df1 dataframe as column and name the column as "cluster
df['clust']=mb

df.head()
'''
Out[18]: 
   Premiums Paid  Age  Days to Renew  Claims made  Income  clust
0           2800   26            233  3890.076336   28000      2
1           2950   27            130  2294.444444   29500      1
2           3100   28            144  2564.545455   31000      1
3           3250   30             65  1978.260870   32500      1
4           3400   32             56  2009.090909   34000      1
'''
###############################################################################
#assign columns as sequence we want
df=df.iloc[:,[1,2,3,4,5]]

df.iloc[:,:].groupby(df.clust).mean()
'''
Out[20]: 
             Age  Days to Renew   Claims made         Income
clust                                                       
0      56.433333     129.466667  21304.646503  151600.000000
1      39.775510      64.551020   5464.794584   81173.469388
2      46.142857     237.761905  16713.571760   80928.571429
#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio
'''
###############################################################################
df.to_csv('Kmeans_insurance.csv',encoding='utf-8')
import os
os.getcwd()    
###############################################################################

'''
Benifits to the client:
    Performing clustering on the insurance policy dataset enables targeted marketing 
    and personalized services, enhancing customer satisfaction and retention while 
    ensuring regulatory compliance.
'''
###############################################################################