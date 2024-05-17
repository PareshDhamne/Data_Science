# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:06:55 2023

@author: PARESH DHAMNE
"""

import pandas as pd

#read the data into a pandas dataframe
df=pd.read_csv("D:/Datasets/Ecommerce_data.csv")
print(df.shape)
df.head(5)
#chexk the distribution of labels
df['label'].value_counts()

#add the new column wgich gives unique number in each of these

df['label_num']=df['label'].map({
    'Household' : 0,
    'Books' : 1,
    'Electronics' : 2,
    'Clothing & Accessories' : 3
    })

#checking the results
df.head(5)
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    df.Text,
    df.label_num,
    test_size=0.2, #20% samples will go to test dataset
    random_state=2022,
    stratify=df.label_num
    )

print("Shape of X_train:" , X_train.shape)
print("Shape of X_test:", X_test.shape)
y_train.value_counts()
y_test.value_counts()
#########################################

#Apply to classifier

from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

#1. create a pipeline object
clf=Pipeline([
    ('vectorizer_tfidf',TfidfVectorizer()),
    ('KNN',KNeighborsClassifier())
    ])

#2.fit with X_train and y_train
clf.fit(X_train,y_train)

#3.get the predictions for x_test and store it in y_pred
y_pred =clf.predict(X_test)

y_pred

#4.print the classification report
print(classification_report(y_test,y_pred))
















from sklearn.feature_extraction.text import TfidfTransformer
