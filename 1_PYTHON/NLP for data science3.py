# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:02:57 2023

@author: Hp
"""
text='Upper PYTHON, lower python, Mixed Python'
import re
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
re.sub('python', matchcase('snake'), text ,flags=re.IGNORECASE)
####################################################################

text='Upper PYTHON, lower python, Mixed Python'
import re
import string
import nltk
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
re.sub('python', matchcase('snake'), text ,flags=re.IGNORECASE)

################################################################

str_pat = re.compile(r'\"(.*)\"')
text1='Computer says "No."'
str_pat.findall(text1)

str_pat = re.compile(r'\"(.*)\"')
text2='Computer says "No." Phone says "Yes."'
str_pat.findall(text2)

str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)

comment =re.compile(r'/\*(.*?)\*/')
text1='/*this is a vomment*/'
comment.findall(text1)

text2='''/*this is a 
multiline comment*/
               '''
comment.findall(text2)
               
comment =re.compile(r'/\*((?:.|\n)*?)\*/')
text2='''/*this is a 
               multiline comment*/
               '''
comment.findall(text2)
##########################################################
import re
def remove_numbers(text):
    result = re.sub(r'\d+','',text)
    return result
input_str="There are 3 balls in this bag, and 12 in the basket."
remove_numbers(input_str)

###########################################
#convert number into word
import inflect 
p= inflect.engine()
#convert number into wwords
def convert_number(text):
    #split string into list of words
    temp_str=text.split()
    #initialise empty list
    new_string=[]
    for word in temp_str:
        #if word is a digit, convert the digit
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
    #append the word as it is
        else:
            new_string.append(word)
    #join the words of  new_string to form a string
    temp_str=' '.join(new_string)
    return temp_str
input_str="There are 3 balls in this bag."
convert_number(input_str)
########################################################

#Exercise 1: Reverse each word of a string

str='My name is Paresh'
a=str.split()
a    
b=" ".join(reversed(a))
b        
'''
def reverse_words(str):
    if str=" ":
        return "You enter wrong input"
    else:
        words=str.split()
        reverse_sentence=" ".join(reversed(words))
    return reverse
print(reverse("My name is Paresh"))
'''
str=input( )
words=str.split()
words   

reverse=" ".join(reversed(words))
reverse 

def reverse_words(sentence):
    words=sentence.split(" ")
    new_word_list=[word[::-1] for word in words]
    res_str=" ".join(new_word_list)
    return res_str
sentence="My name is King"
reverse_words(sentence)

##########################################################

#Exercise 2:Read text file into a variable and replace
with open("sample.txt",'r') as file:
     content=file.read()
single_line=content.replace('\n',' ')
print(single_line)
##########################################################





     