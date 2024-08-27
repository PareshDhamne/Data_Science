# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:07:54 2024

@author: Hp
"""
import pandas as pd

df=pd.read_csv("D:/SUPERVISED ALGORTIHM/GRADIENT BOOSTING/movies_classification.csv")

#dummy variables
df.head()
df.info()

#n-1 dummy variables will be created for n categories

df=pd.get_dummies(df,columns=["3D_available","Genre"],drop_first=True)

df.head()

#Input and output Split
predictors = df.loc[:,df.columns!="Start_Tech_Oscar"]
type(predictors)

target=df["Start_Tech_Oscar"]

#Train Test partition of the data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)

from sklearn.ensemble import GradientBoostingClassifier
boost_clf=GradientBoostingClassifier()
boost_clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

confusion_matrix(y_test,boost_clf.predict(X_test))
accuracy_score(y_test,boost_clf.predict(X_test))

#Hyperparameters
boost_clf2=GradientBoostingClassifier(learning_rate=0.02,
                                        n_estimators=1000,
                                        max_depth=1)
boost_clf2.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#Evalution on testing data
confusion_matrix(y_test,boost_clf2.predict(X_test))
accuracy_score(y_test,boost_clf2.predict(X_test))

#Evalution on training data
accuracy_score(y_train,boost_clf2.predict(X_train))
