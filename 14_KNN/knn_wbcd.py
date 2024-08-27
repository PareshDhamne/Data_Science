# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:59:04 2024

@author: Paresh Dhamne
"""

import pandas as pd
import  numpy as np
import seaborn as sns
wbcd=pd.read_csv("D:/SUPERVISED ALGORTIHM/KNN/wbcd.csv")
#there are 569 rows and 32 columns
##################################################

#EDA
wbcd.shape

wbcd.describe()

wbcd.isnull().sum()
#there is no null value in dataset
###################################################

sns.boxplot(wbcd)
#data is containing the outlier and data is imbalanced.
#################################################

wbcd.describe()
#in output colimn there is only B for Benien and M for Malignant
#############################################################
#let us first convert it as Benign and Malignant
wbcd['diagnosis']=np.where(wbcd['diagnosis']=='B','Beniegn',wbcd['diagnosis'])
#in wbcd there is column named 'diagnosis' , where ever there is 'B' replace with 'Beniegn'

#similarly where ever there is M in the same column replace with 'Maligant
wbcd['diagnosis']=np.where(wbcd['diagnosis']=='M','Malignant',wbcd['diagnosis'])
#######################################

#oth column is patient ID let us drop it
wbcd=wbcd.iloc[:,1:32]
wbcd
#########################################

#normalization

def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now let us apply this function to the dataframe
wbcd_n=norm_func(wbcd.iloc[:,1:32])

#because now 0th column is output or label it is not considered

######################################

#let us apply X as input and y as output
X=np.array(wbcd_n.iloc[:,:])
#since in wbcd_n, we are already excluding output column, hence ll rows and columns
y=np.array(wbcd['diagnosis'])
#########################################

#Now let us split the data into training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

#here you are passing X,y insted dataframe handle
#there could chances of unbalancing od data.
#let us assume you have 100 datapoints out of which 80NC and 20 cancer
#these data points must be equally distributed
#there is satisfied sampling concep is usedd

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=21)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
pred

#now let us evaluate the model
from sklearn.metrics import accuracy_score
print(accuracy_score(pred,y_test))
pd.crosstab(pred,y_test)
#let us check the applicability of the model
#ie.miss classification, Actual patient is malignant
#i.e. cancer patient but predicted is benien is 1
#actual patient is Benien and predicted as cancer patient is 5
#hence this model is not acctable
##############################################3

#let us try to select correct value of k
acc=[]
#running KNN algorithm for k=3 to 50 in the step of 2
#k value selected is odd value

for i in range(3,50,2):
    #declare the mdoel
    neigh=KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train,y_train)
    train_acc=np.mean(neigh.predict(X_train)==y_train)
    test_acc=np.mean(neigh.predict(X_test)==y_test)
    acc.append([train_acc,test_acc])
    
#if you will see the acc, it has got two accuracy, i[0]-train_acc
#i[1]=test_acc
#to plot the graph of train_acc and test_acc
import matplotlib.pyplot as plt
plt.plot(np.arange(3,50,2),[i[0] for i in acc],'ro-')
plt.plot(np.arange(3,50,2),[i[1] for i in acc],'bo-')
#there are 3,5,7 and 9 are possible values where accuracy is good
#let us check for k=3
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
accuracy_score(pred,y_test)
pd.crosstab(pred,y_test)
##########################################################
#ie.miss classification, actual patient is malignant
#i.e.cancer patient but predicted is benien is 1
#actual patient is benien and predicted as cancer patient is 2
#hence this model is not acceptable
#for 5 same sinario
#for k=7 we are getting zero false positive and good accuracy
#hence k=7 is appropriate value of k