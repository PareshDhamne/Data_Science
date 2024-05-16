# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:10:43 2023

@author: Hp
"""

from sklearn.feature_extraction.text import TfidfTransformer

corpus = ["Thor eating pizza, Loki is eating pizza, Ironman ate pizza already",
          "Apple is announcing new (phane tomorrow",
          "Tesla is announcing new model-3 tomorrow",
          "Google is announcing new pixel-6 tomorrow",
          "Microsoft is announcing new surface tomorrow",
          "Amazon is announcing new eco-dat tomorrow",
          "I an eating biryant and you are eating grapes"
]

from sklearn.feature_extraction.text import TfidfVectorizer

v = TfidfVectorizer()
v.fit(corpus)
transform_output = v.transform(corpus)

#print vocabulary
print(v.vocabulary_)
#print list list of each word
all_features_name = v.get_feature_names_out()
for word in all_features_name:
    #get the index in the vocabulary
    indx=v.vocabulary_get(word)
    #get the score
    idf_score=v.idf_[indx]
    print(f"{word}:{idf_score}")