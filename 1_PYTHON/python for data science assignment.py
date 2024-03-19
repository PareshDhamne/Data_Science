# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:56:38 2023

@author: Hp
"""

#ASSIGNMENT
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cars=pd.read_csv("D:/PARESH1_python/Cars_csv.csv")
cars
cars.columns
cars.describe()

#
plt.hist(cars.speed)
sns.displot(x='speed',kde=True,bins=6,data=cars)
#there are almost 14 cars which have spped btween 10.5 to 14.5
#it is left skewed because left side very long
#there 12 cars whicha re 
sns.displot(x='dist',kde=True,bins=6,data=cars)
#there are 17.5 no of cars which travelling distancebetween 21 to 41
#it is right skewed because right side is very long

sns.boxplot(cars.speed)
#the mean speed of all cars was 15
#
plt.hist(cars.dist)
#it is right skew

sns.boxplot(cars.dist)
#here diamond is representing a oulier which is very far from 100

#kewness of a speed
speed=cars['speed'].tolist()
speed
print("Skewness of Speed",skew(speed))
dist=cars['dist'].tolist()
print("Skewness of dist",skew(dist))
print(skew(dist,axis=0,bias=True))
#it signifies thag distribution is positi
print(kurtosis(dist,axis=0,bias=True))

#Bar graph
sns.countplot(x='speed',data=cars)

#sns.countplot(x='speed',hue='',data=cars,palette='set1')

#kdt plot
sns.kdeplot(x='dist',data=cars,color='black')

#scatter plot
sns.scatterplot(x='speed',y='dist',data=cars)
#we cans see that most of the cars are at speed betwwen 10 to 20 and distance less than 80
#there are very less cars who has speed less than 5

#joint plot
sns.jointplot(x='speed',y='dist',data=cars,kind='reg')

#pairplot()
sns.pairplot(cars)

#A heat map
corr=cars.corr()
sns.heatmap(corr)


#assignment 2 for iris data set
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('iris')
df.head
df.columns
df.describe()
'''
data sdictionary
sepal_length
sepal_width
petal_lenght
petsl_width
'''
plt.hist(df.sepal_length)
plt.hist(df.sepal_width)
plt.hist(df.petal_length)
plt.hist(df.petal_width)
sns.displot(x='sepal_length',kde=True,bins=6,data=df)
#more than 35 iris has petal length between 5.5 to 6.2
#it is right skew

sns.displot(x='petal_length',kde=True,bins=6,data=df)
#this is the 
sns.displot(x='sepal_width',kde=True,bins=6,data=df)
sns.displot(x='petal_width',kde=True,bins=6,data=df)

#boxplot
sns.boxplot(df.sepal_length)
sns.boxplot(df.sepal_width)
sns.boxplot(df.petal_length)
sns.boxplot(df.petal_width)

#kewness
df1=df['sepal_length'].tolist()
print("Skewness of sepal_length ",skew(df1))
print(skew(df1,axis=0,bias=True))
print(kurtosis(df1,axis=0,bias=True))

df2=df['sepal_width'].tolist()
print("Skewness of sepal_width",skew(df2))
print(skew(df2,axis=0,bias=True))
print(kurtosis(df2,axis=0,bias=True))

df3=df['petal_length'].tolist()
print("Skewness of petal_length",skew(df3))
print(skew(df3,axis=0,bias=True))
print(kurtosis(df3,axis=0,bias=True))

df4=df['petal_width'].tolist()
print("Skewness of petal_width",skew(df4))
print(skew(df4,axis=0,bias=True))
print(kurtosis(df4,axis=0,bias=True))

#BAr graph
sns.countplot(x='sepal_length',data=df)
sns.countplot(x='sepal_width',data=df)
sns.countplot(x='petal_length',data=df)
sns.countplot(x='petal_width',data=df)

#kdt plot
sns.kdeplot(x='sepal_length',data=df,color='black')
sns.kdeplot(x='sepal_width',data=df,color='black')
sns.kdeplot(x='petal_length',data=df,color='black')
sns.kdeplot(x='petal_width',data=df,color='black')

#scatter plot
sns.scatterplot(x='sepal_length',y='petal_width',data=df)

#joint plot
sns.jointplot(x='sepal_length',y='petal_width',data=df,kind='reg')

#pairplot()
sns.pairplot(df)

#A heat map
corr=df.corr()
sns.heatmap(corr)


