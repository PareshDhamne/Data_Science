# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:51:14 2023

@author: Hp
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
 
corpus=['The mouse had a tiny Little mouse',
        'The cat saw the mouse', 'The cat catch the mouse',
        'The end of mouse story']

#step1 initilize the count vector
cv=CountVectorizer()
#to count the total no.of TF

word_count_vector=cv.fit_transform(corpus)
word_count_vector.shape

#next step apply idf
tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(word_count_vector)

#this above matrix is in raw form lets convert to dataframe
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names_out() , columns=['idf_weights'])

#sort ascending
df_idf.sort_values(by=['idf_weights'])
#notice that the word mouse has lowest frequency,
