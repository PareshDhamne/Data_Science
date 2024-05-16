# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:11:42 2023

@author: Paresh Dhamne

PROBLEM STATEMENT:
    Applying hierarchical and K-means clustering on wine data, followed by PCA for dimensionality 
    reduction, enables comparison of clustering results, aiding in optimizing wine quality and 
    production costs while ensuring consistency in quality delivery.
    

Business Objective:

    maximize: Providing good quality medicines to the patient to reduce heart diseases.

    minimize: minimize The loss of information during the reduction process.

Business Constraints:  
    Constraints: Maintaining the result,Data Privacy and Ethics

#in given wine dataset
1. 'age':
   - representing age of patient.
   - ordinal data.
2. 'sex':
   - representing the sex of patient.
   - nominal data
3. 'cp':
   - representing the patients having chest pain.
   - nominal data
4. 'trestbps':
   - representing the resting blood pressure (in mm Hg on admission to the hospital).
   - ordinal data
5. 'chol':
   -representing the serum cholestoral in mg/dl.
   -ordinal data
6. 'fbs':
   - representing the fasting blood sugar &gt; 120 mg/dl (1 = true; 0 = false).
   - nominal data
7. 'restecg':
   - representing the resting electrocardiographic results.
   - nominal data
8. 'thalach':
   - representing the maximum heart rate achieved.
   - ordinal data
9. 'exang':
   - representing the exercise induced angina (1 = yes; 0 = no).
   - nominal data
10. 'oldpeak':
    - representing the ST depression induced by exercise relative to rest.
    - ordinal data
11. 'slope':
    - representing the the slope of the peak exercise ST segment.
    - nominal data
12. 'ca':
    - representing the number of major vessels (0-3) colored by flourosopy.
    - nominal data
13. 'thal':
    - representing 1 = normal; 2 = fixed defect; 3 = reversable defect.
    - nominal data

"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('D:/ASSOCIATION/heart disease.csv')
df
###########################################
#EDA
df.columns
'''
Index(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'],
      dtype='object')
'''
#########################################

df.dtypes
'''
age           int64
sex           int64
cp            int64
trestbps      int64
chol          int64
fbs           int64
restecg       int64
thalach       int64
exang         int64
oldpeak     float64
slope         int64
ca            int64
thal          int64
target        int64
dtype: object

all datatpes are numerical containing float and int values
'''
##########################################
a=df.describe()
a
# there scale diffrence in mean and std and the mean and median are  near approx same
# but show some variaion as the standard deviation is showing diffrence with mean
# so the datapoints are scatter from median
##########################################
# Check for the null values
n=df.isnull()
n.sum()
'''
age         0
sex         0
cp          0
trestbps    0
chol        0
fbs         0
restecg     0
thalach     0
exang       0
oldpeak     0
slope       0
ca          0
thal        0
target      0
dtype: int64

The dataframe doesn't contain any null value'
'''
#############################################

# Visualize the Data
# To undestand the corelaion between the datapoints and the columns we plot
# some plots

import seaborn as  sns

sns.pairplot(df)
# from the pairplot observe that the data is more scatter and the relation between
# the columns are quite similar

# To identify if there is any outlier in columns we plot the boxplot
sns.boxplot(df)
# # the trestbps,chol and thalach column contain the outlier

# to analyze whether the columns follow pattern or not we draw the heatmap 

corr=df.corr()
sns.heatmap(corr)
# from the heamap i can understand that the diagonal colour of are same so the 
# columns follow some pattern 
####################################################

# So there is outlier is present and also the the column shows skewness propery
# and there is scale difference in mean and std so we use standardization technique as we are going to use 
# PCA

# Standardization
# initialize the scalar
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
df=scalar.fit_transform(a)
dataset=pd.DataFrame(df)
res=dataset.describe()
# in the resvariable we will see that the mean value is almost value 
#Standard deviation is zero
#################################################

# Model Building

#For visualzing the cluster of  the above dataframe we  have to draw
# Dendodron first then we cluster the datapoints

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

# linkage function give the hierarchical and Agglomotive clustering
 

z=linkage(dataset,method='complete',metric='euclidean')

plt.figure(figsize=(15,8))
plt.title('Hierarchical Clustering')
plt.xlabel('Index')
plt.ylabel('Disance')
#sch is help to draw 
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#appying agglomerative clustering choose 1 as a cluster from dendogram

# In dedrogram is not show the clustering it only shows how many clusters are there

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=2,linkage='complete',affinity='euclidean').fit(dataset)

#apply labels to the cluster
h_complete.labels_
# so these all are in the form of array we have to convert the Series
cluster_labels=pd.Series(h_complete.labels_)
# so these all are in the form of array we have to convert the Series
cluster_labels=pd.Series(h_complete.labels_)

df['clust']=cluster_labels
df
####################################################

# K-Means Clustering
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df=pd.read_csv('wine.csv')
df
TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(dataset)
    
    TWSS.append(kmeans.inertia_)
    
    '''
    kmeans inertia also known as sum odf sqares methos
    .It measures all the datapoints from the centroid of the point.
    it differentiate between observed value and predicted value
    '''
    
TWSS
# Plot a elbow curve
plt.plot(k,TWSS,'ro-')
plt.xlabel('No of clusers')
plt.ylabel('Total within SS')

model=KMeans(n_clusters=3)
model.fit(dataset)
model.labels_
mb=pd.Series(model.labels_)
type(mb)
df['clust']=mb
df.head()
d=df.iloc[:,[5,0,1,2,3,4]]
d
########################################

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

#Normalize the numeric data
uni_normal=scale(df)
uni_normal

pca=PCA(n_components=3)
pca_values=pca.fit_transform(uni_normal)

#The amount of variance that each PCA explain

var=pca.explained_variance_ratio_
var

#Commulative Variance
var1=np.cumsum(np.round(var,decimals=4)*100)
var1
#Variance plot for PCA component obtained
plt.plot(var1,color='red')
#PCA Scores
pca_values

pca_data=pd.DataFrame(pca_values)
pca_data.columns='comp0','comp1','comp2'

final=pd.concat([df.clust,pca_data],axis=1)

#Visualize the dataframe
ax=final.plot(x='comp0',y='comp1',kind='scatter',figsize=(12,8))
final[['comp0','comp1','clust']].apply(lambda x:ax.text(*x),axis=1)

####################################################################
'''
Benifits to the client:
    By employing hierarchical and K-means clustering on heart disease data followed by PCA for 
    dimensionality reduction, the project aims to enhance medication quality for heart diseases 
    while minimizing information loss. It facilitates comparison of clustering outcomes, optimizing 
    healthcare delivery, and upholding data privacy and ethical standards.
    
'''