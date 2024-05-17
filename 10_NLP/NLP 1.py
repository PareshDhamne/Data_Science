# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:25:48 2023

@author: PARESH DHAMNE
"""

sentence="We are Learning Textmining from Sanjivani AI"
##if we want to know the position of learning

sentence.index("Learning")

#it will show learning is at position of learning
#this is going to show character position from 0 to ***
###############################################

#we want  to know position textmining word
sentence.split().index("Textmining")
#it will split the words in list and count the position
#if you want to see the list select sentence.split()
#it will show 3
##############################################

#suppose we want to print any word in reverse order
sentence.split()[2][::-1]
#[start:end end:-1(start)] will start form -1 -2 till the end
#learning will be printed ad gninrael.
##############################################

#suppose we want to print first and last word of sentence
words=sentence.split()
first_word=words[0]
first_word

last_word=words[-1]
last_word
##########################################

#now we want ot concate the first and last word
concat_word=first_word+"  "+last_word
concat_word

#####################################
#we want to print even words from the sentence

[words[i] for i in range(len(words))if i%2==0]

##########################################

#we want to display only ai
sentence
sentence[-3:]

#suppose we want to display entire sentence in reverse order

sentence[::-1]
##########################################

#suppose we want to select each word and print in reverse order
words
print(" ".join(word[::-1] for word in words))
###########################################

#tokenization 
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading Python")
words
################################