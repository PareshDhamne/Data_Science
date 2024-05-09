# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 08:29:51 2023

@author: Paresh Dhamne

Problem:
    Perform clustering on mixed data. Convert the categorical variables to numeric by using dummies 
    or label encoding and perform normalization techniques. The data set consists of details of customers related 
    to their auto insurance. Refer to Autoinsurance.csv dataset.

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
##############################################################################
import pandas as pd
import matplotlib.pyplot as plt

#now import file from data sett and create a dataframe
df=pd.read_csv("D:/Datasets/AutoInsurance.csv")
##############################################################################
df.describe()
'''
       Customer Lifetime Value  ...  Total Claim Amount
count              9134.000000  ...         9134.000000
mean               8004.940475  ...          434.088794
std                6870.967608  ...          290.500092
min                1898.007675  ...            0.099007
25%                3994.251794  ...          272.258244
50%                5780.182197  ...          383.945434
75%                8962.167041  ...          547.514839
max               83325.381190  ...         2893.239678
It gives 5 number summary
'''
############################################################################

df.shape
#Out[11]: (9134, 24)
###########################################################################

df.columns
'''
Out[13]: 
Index(['Customer', 'State', 'Customer Lifetime Value', 'Response', 'Coverage',
       'Education', 'Effective To Date', 'EmploymentStatus', 'Gender',
       'Income', 'Location Code', 'Marital Status', 'Monthly Premium Auto',
       'Months Since Last Claim', 'Months Since Policy Inception',
       'Number of Open Complaints', 'Number of Policies', 'Policy Type',
       'Policy', 'Renew Offer Type', 'Sales Channel', 'Total Claim Amount',
       'Vehicle Class', 'Vehicle Size'],
      dtype='object')
'''
##########################################################################

#we have one column 'award' which really not useful we will drop it
df1=df.drop(['Education','Customer','Policy'],axis=1)
df1.shape
df1.columns
df1.dtypes
'''
Out[17]: 
State                             object
Customer Lifetime Value          float64
Response                          object
Coverage                          object
Effective To Date                 object
EmploymentStatus                  object
Gender                            object
Income                             int64
Location Code                     object
Marital Status                    object
Monthly Premium Auto               int64
Months Since Last Claim            int64
Months Since Policy Inception      int64
Number of Open Complaints          int64
Number of Policies                 int64
Policy Type                       object
Renew Offer Type                  object
Sales Channel                     object
Total Claim Amount               float64
Vehicle Class                     object
Vehicle Size                      object
dtype: object
'''
#########################################################################
#we know that there is scale difference among the columns, which we have to remove
#either by using normalization or standardization
#whenever there is mixed data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normalization function to df1 dataframe for first 15 rows
df_norm=norm_func(df1.iloc[:,:])
df_norm
###########################################################################

#you can check the df_norm dataframe which is scaled between values from 0 to 1
#you can apply describe function to new dataframe
b=df_norm.describe()
b
########################################################################
# plot dendrogram first
#now to create dendrogram we need to measure distance,

#we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

#linkage function  gives us hirerarchical or Agglomotive clustering
#ref the help for linkage
z=linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8));
plt.title("Hirerchical Clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
#######################################################################
#applying agglomerative clustering choosing 3 as clusetrs from dendrogram


from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)
#apply labels to the clusters

h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)

#assign thsi series to univ dataframe as column and name the column as "cluster
df1['clust']=cluster_labels

df=df1.iloc[:,[21,19,18,17,1,3,4,5,6,7,9,10,2,8,11,12,13,14,15,16,20]]

df.iloc[:,:].groupby(df.clust).mean()

#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio
########################################################################
df.to_csv("autoinsurence assignment.csv",encoding='utf-8')
import os
os.getcwd()
##############################################################
'''
Benifits to the client:
    the benefit to the client is the ability to identify high-risk 
    policyholders and tailor personalized insurance offerings to maximize 
    customer satisfaction and retention, leveraging insights from 
    clustering analysis on mixed data with appropriate normalization techniques.
'''
##########################################################################