# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:15:53 2023

@author: Hp
"""

#bag of words
#this bow convrts unstructured data to structured form

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['At least seven indian pharma companies are working to develop vaccine against the corona virus.',
        'The deadly virus that has already infected more than 14 million globally ',
        'Bharat Biotech is the among the domestic pharma firm working on the corona virus vaccine in India']
bag_of_word_model=CountVectorizer()
print(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_df=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())

bag_of_word_df.columns=sorted(bag_of_word_model.vocabulary_)
bag_of_word_df.head()

##########################################

#bag of word model small
bag_of_word_model_small=CountVectorizer(max_features=5)
bag_of_word_df_small=pd.DataFrame(bag_of_word_model_small.fit_transform(corpus).todense())
bag_of_word_df_small.columns=sorted(bag_of_word_model_small.vocabulary_)
bag_of_word_df_small.head()
###################################################