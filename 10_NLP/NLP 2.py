# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:25:27 2023

@author: Paresh Dhamne
"""

'''Text- minimng'''

###############
# fiinding the index of the letter
senctence="we are learning textmining from Sanjivani AI"
# if we want to know position of learning
senctence.index("learning")
# it will show learning is at the 7 position
# this is going to show thw charater position from 0  inculding

###################################
# finding the position of the words
# we want to know postion textminig word
senctence.split().index('textmining')
#it will split the words  in list  and count the position
# if you want to see the list select senectence.split() and
# it will show at 3

############################################################
#suppose we want print any word in the reverse order
senctence.split()[2][: :-1]
# [start:end end:-1 (start)]  will start from -1,-2,-3 till the end
#learnig will be printed in the reverse order

################################################
# suppose we want to print first and last word of the sentence
words=senctence.split()
first_words=words[0]
first_words
last_words=words[-1]
last_words

##########################################
# now we want to concate the first and last words
concate_word=first_words+" "+last_words
concate_word
###########################################
# we want the to print  even words from the sentence
[words[x] for x in range(len(words)) if x%2==0]
# the words having the odd length are not print
##############################################
senctence
# now we want to display only ai
senctence[-3:]
# balaji  publication
############################################
# suppose we want to display the entire sentence in the revrese order
senctence[::-1]
# now the all the sentence are print in the reverse order

##########################################
# suppose we want to select each word and print in the reverse order
words
print(" ".join(word[::-1] for word in words))
# 


#############################################################
''' ********************tokenization*******************************'''
import nltk
nltk.download('punkt')          # it is install here only
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)
# it is split the hole sentance into each words


###################################################################
#day 21/11/23

#parts of speech (POS) tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
# it is going mention parts of speech
############################################################
# stop words from nltk library
from nltk.corpus import stopwords
stop_words= stopwords.words("English")
#you can verify 179  stop words in varible explorer
print(stop_words)
sentence1= "I am learning NLP: It is one of the most popular like"
# first we will tokenize the sentance
sentence_words= word_tokenize(sentence1)
print(sentence_words)
##remove the stop_words from the sentance
# now let us filter the sentance1 using stop_words
sentence_no_stops=" ". join([words for words in sentence_words if words not in stop_words])
print(sentence_no_stops)
sentence1
# you can notice that am , is , of, the , most, popular, in are missing from the result
###################################################
# suppose we want to replace words in string
sentence2= 'I visited My from IND on 14-02-19'
normalized_sentence=sentence2.replace("My","Malaysia"). replace("IND", "India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)
###############################################
#suppose  we want auto correction in the sentence
from autocorrect import Speller
#install the autocorrect 
# declare the function speller definned for english
spell=Speller(lang='en')
spell("Enilish")
######################################
# suppose we want to correct the whole sentence
sentence3= "Ntural lanagage processin deals withh the aart of extracting sentiiiments"
# let us first tokenize sentence
sentence3= word_tokenize(sentence3)
corrected_sentence =" ". join ([spell(word) for word in sentence3])
print(corrected_sentence)
spell("Suitm")

