# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:22:54 2024

@author: Hp
"""

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

### Loading data

email_data=pd.read_csv("D:/SUPERVISED ALGORTIHM/NAVIE BAYES/sms_raw_NB.csv",encoding="ISO-8859-1")

##################CLEANING DATA

import re

def cleaning_text(i):
    w=[]
    i=re.sub("[^A-Za-z""]+"," ",i).lower()
    for word in i.split(" "):
        if len(word)>3:
            w.append(word)
    return (" ".join(w))

################# Testing above function with some text
cleaning_text("Hope you are having good week.just checking")
cleaning_text("hope i can understand your feelings 123121.123. hi how are you?")
cleaning_text("hi how are you,I am sad")
email_data.txt=email_data.text.apply(cleaning_text)
email_data.txt

email_data=email_data.loc[email_data.text != "",:]
from sklearn.model_selection import train_test_split
email_train,email_test=train_test_split(email_data,test_size=0.2)

### creating matrix of token counts for entrie text document

def split_into_words(i):
    return[word for word in i.split(" ")]

emails_bow=CountVectorizer(analyzer=split_into_words).fit(email_data.text)
all_emails_matrix=emails_bow.transform(email_data.text)

###for training messages
train_emails_matrix=emails_bow.transform(email_train.text)

test_emails_matrix=emails_bow.transform(email_test.text)
##learning term weighttaging and normaling on entire emails
tfidf_transformer=TfidfTransformer().fit(all_emails_matrix)
tfidf_transformer

###preparing TFIDF fro train_mails
train_tfidf=tfidf_transformer.transform(train_emails_matrix)

###preparing TFIDF for test_mails
test_tfidf=tfidf_transformer.transform(test_emails_matrix)
test_tfidf.shape

###Now let us apply this toNAvie Bayes

from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb=MB()
classifier_mb.fit(train_tfidf,email_train.type)
###evalution on test data

test_pred_m=classifier_mb.predict(test_tfidf)
accuracy_test_m=np.mean(test_pred_m==email_test.type)
accuracy_test_m
