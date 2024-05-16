# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 08:56:28 2023

@author: PARESH DHAMNE
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#let us try to understand first how k means works for two dimensional data
#for that, generate random numbers in the range 0 to 1
#and with uniform probability of 1/50
x=np.random.uniform(0,1,50)
y=np.random.uniform(0,1,50)

#create a empty dataframe with 0 rows and 2 columns

df_xy=pd.DataFrame(columns=["x","y"])
#assign two values of x and y to these columns

df_xy.x=x
df_xy.y=y

df_xy.plot(x='x',y='y',kind="scatter")
model1=KMeans(n_clusters=3).fit(df_xy)

'''
with data x and y, apply kmeans model,
generate scatter plot
with scale /font=10

cmap=plt.cm.coolwaem:cool color combination

'''

Univ1 =pd.read_excel('D:/Datasets/University_Clustering.xlsx')
Univ1.describe()
Univ=Univ1.drop(['State'],axis=1)

# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normlization function to Univ dataframe gor all the rows

df_norm=norm_fun(Univ.iloc[:,1:])

#what will be ideal cluster number will it be 1,2,3

TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
TWSS
#as k value increases the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters");
plt.ylabel("Total_within_SS");

'''
How to select  value of k from elbow curve
when k changes from 2 to 3 then decreases
in twss in higher than
when k changes from 3 to 4
when k values changes from 5 to 6 decrease
in twss is considerably less, hence considered k=3
'''

model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
Univ['clust']=mb
Univ.head()
Univ=Univ.iloc[:,[7,8,1,2,3,4,5,6]]
Univ
Univ.iloc[:,2:8].groupby(Univ.clust).mean()
Univ.to_csv('Kmeans_UNiversity.csv',encoding='utf-8')
import os
os.getcwd()    
