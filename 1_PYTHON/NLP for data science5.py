# -*- coding: utf-8 -*-
"""
Created on Fri May 26 08:21:59 2023

@author: Hp
"""

import nltk
nltk.download('punkt')
sentence_data="The First sentence is about Python. The Second:about Django. You can learn Pyhton, Django here."
nltk_tokens=nltk.sent_tokenize(sentence_data)
print(nltk_tokens)
########################################

#non_english Tokensization
import nltk
german_tokenizer=nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenizer.tokenize('Wie geht es Ihnen? Gut, danke.' )
print(german_tokens)
#######################################

#word tokenization
import nltk
word_data="It originated from the idea that there are readers who prefer learning new skills from you."
nltk_tokens = nltk.word_tokenize(word_data)
print(nltk_tokens)
########################################

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words('english')
