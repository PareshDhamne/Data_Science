# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:19:16 2024

@author: Paresh Dhamne

1.	Business Problem
1.1.	What is the business objective?
    1.1.1.Maximize: Ensure that each species has an environment that closely mimics its natural
                       habitat, promoting physical and mental well-being.
    1.1.2.Minimize:Minimize stress by avoiding overcrowding and providing hiding 
                        spots or separate areas for animals that may be prone to aggression.
1.2.	Are there any constraints?
          Ensure that the design and layout of the zoo prioritize visitor safety while 
              maintaining a close and informative interaction with the animals.
          
DATA DICTIONARY:
animal name: contains name of animal is nominal data.
hair: contains the hair is there or not for animal is quantitative data.
feathers: quantitative data
eggs: quantitative data
milk:quantitative data
airbone: quantitative data
predator:quantitative daat
type : is target variable is numrical data
"""

import pandas as pd
import  numpy as np
import seaborn as sns
zoo=pd.read_csv("D:/SUPERVISED ALGORTIHM/KNN/Zoo.csv")

##################################################

#EDA
zoo.shape
#(214, 10)

zoo.describe()
#provides 5 number summary

zoo.isnull().sum()
#there is no null value in dataset
###################################################

sns.boxplot(zoo)
#data is containing the outlier and data is imbalanced.
################################################

#animal name is not important so drop that column
zoo = zoo.drop('animal name',axis=1)

#########################################

#normalization

def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now let us apply this function to the dataframe
zoo_n=norm_func(zoo.iloc[:,0:16])

#because now 10th column is output or label it is not considered
zoo['type']
######################################

#let us apply X as input and y as output
X=np.array(zoo_n.iloc[:,:])
#since in glass_n, we are already excluding output column, hence all rows and columns
y=np.array(zoo['type'])
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