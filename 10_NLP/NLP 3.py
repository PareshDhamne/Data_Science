# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:09:58 2023

@author: PAresh Dhamne
"""
import nltk
nltk.download('punkt') 
from nltk import word_tokenize

words=word_tokenize("I am reading NLP Fundamentals") 
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
#####################################################

#22 nov 2023

##STEMMING
stemmer=nltk.stem.PorterStemmer()
stemmer.stem('Programming')
stemmer.stem('Programmed')
stemmer.stem('Jumping')
stemmer.stem('Jumped')
##############################################

#Lemitizer
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize('programmed')
lemmatizer.lemmatize('programs')
lemmatizer.lemmatize('battling')
lemmatizer.lemmatize('amazing')
##################################################


#23 nov 2023
#churking (shallow Paesing) idenitfying name entity
nltk.download("maxent_ne_chunker")
nltk.download('words')

sentence4="We are learning NLP in python by SanjivaniAi"

#first we will tokenize
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]
##############################################

#SENTENCE TOKENIZATION
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are Learning NLP in Python. Delivered by SanjivaniAI. Do you know where it is located? It is in Kopargaon.")
sent
############################################

from nltk.wsd import lesk
sentence1="Keep your savings in the bank"
print(lesk(word_tokenize(sentence1),'bank'))

sentence2="It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))

#Synset('bank.v.07') a slope in the turn of road or truck
#the outside is higher then the inside in order to reduce the 
#"bank" as multiple meanings. If you want tov find exact meaning
#execute following code
#the defination for bank can be seen here:
    
from nltk.corpus import wordnet as wn
for ss in wn.synsets('bank'):print(ss,ss.definition())
###########################################

import re
sentence5='"sharat twitted ,wittnessing 70th republic day India from Rajpath ,\new Delhi ,Mesmorizing performance by Indian Array!"'
re.sub(r'([^\s\w]|_)+', ' ',sentence5).split()

##extracting n gram
#n-gram can be extracted using three technique
#1.custom defined function
#2.Nltk
#3.TextBlob
################################################

#extracting n-grams usning custom definef]d function

import re
def n_gram_extractor(input_str,n):
    tokens=re.sub(r'([^\s\w]|_)+', ' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])

n_gram_extractor("The cute Little boy is playing with kitten",2)
n_gram_extractor("The cute Little boy is playing with kitten",3)
######################################################

from nltk import ngrams#
#extraction n-gram with nltk
list(ngrams('The cute Little boy is playing with kitten'.split(),2))
list(ngrams('The cute Little boy is playing with kitten'.split(),3))
################################################

from textblob import TextBlob
blob=TextBlob("The cute Little boy is playing with kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)
####################################################

###tokenization using keras,
sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)
###############################################

#tokenization using textblob
from textblob import  TextBlob
blob=TextBlob(sentence5)
blob.words

########################################

#tweet Tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)

#######################################

#multi word expression
from nltk.tokenize import MWETokenizer
sentence5
mwe_tokenizer=MWETokenizer(['republic','day'])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('/',' ').split())

###################################

#regurler expression tokenizer
from nltk.tokenize import RegexpTokenizer
reg_tokenizer=RegexpTokenizer('\w+|\$[\d\.]+|\S+')
reg_tokenizer.tokenize(sentence5)
###################################

#white space tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence5)
################################

from nltk.tokenize import WordPunctTokenizer
wp_tokenizer=WordPunctTokenizer()
wp_tokenizer.tokenize(sentence5)
#############################################

sentence6="I love playing cricket.Cricket players practices hard in their inning"
from nltk.stem import RegexpStemmer
regex_stemmer=RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd) for wd in sentence6.split())
###################################################

sentence7="Before eating , it would be nice to sanitize your hands with a sanitizer"
from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()
words=sentence7.split()
" ".join([ps_stemmer.stem(wd) for wd in words])
#################################################

#Lemmmitixzation
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
sentence8="The codes executed today are for better than what we execute generally"
words=word_tokenize(sentence8)
" ".join([lemmatizer.lemmatize(word) for word in words])
############################################

#singularize and pluralization
from textblob import TextBlob
sentence9=TextBlob("She sells seashells on the seashare")
words=sentence9.words#we want to make word[2] i>e. seashells in singular form
sentence9.words[2].singularize()
#we want word $ i.e. seashare in plural form 
sentence9.words[5].pluralize()
######################################################

#language translation from spaniah to English
from textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es',to='en')
#############################################

#custom stopwords removal
from nltk import word_tokenize
sentence9="She sells seashells on the seashare"
custom_stop_word_list=['she','on','the','am','is']
words=word_tokenize(sentence9)
" ".join([word for word  in words if word.lower() not in custom_stop_word_list])
#select words which is not defined in list
##########################################

##############################25 Nov 2023#######################################

#extracting general features from raw text
#number of words
#detect presence of wh word
#polarity
#subjectivity
#language identification
#####################################

#to identify the number of words
import pandas as pd
df=pd.DataFrame([['The vaccine for covid-19 will be announced on 1 st August '],
                 ['Do you know how much expections the world population is having from this research?'],
                 ['The risk of virus will come to an end on 31st July']
                 ])
df.columns=['text']
df

#now let us measure the number of words
from textblob import TextBlob
df['number_of_words']=df['text'].apply(lambda x:len(TextBlob(x).words))
df['number_of_words']
########################################

#Detect presence of word wh
wh_words=set(['why','who','which','what','where','when','how'])

df['is_wh_words_present']=df['text'].apply(lambda x:True if len(set(TextBlob(str(x)).words).intersection(wh_words))>0 else False)
df['is_wh_words_present']
##########################################

#polarity of the sentence
df['polarity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']

sentence10='I like this example very munch'
pol=TextBlob(sentence10).sentiment.polarity
pol

sentence10='This is fantastic example and I like it very much'
pol=TextBlob(sentence10).sentiment.polarity
pol

sentence10='This was helpful example but I would have prefer another one'
pol=TextBlob(sentence10).sentiment.polarity
pol

sentence10='This is my personal opinion that it was helpful example but I would prefer another one'
pol=TextBlob(sentence10).sentiment.polarity
pol
#########################################

#subjectivity of the dataframe df and check whetehr there is personal openion or not

df['subjectivity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['subjectivity']
######################################

#To find language of  the sentence this part of code will get http error
df['language']=df['text'].apply(lambda x:TextBlob(str(x)).detect_language())

#######################################





