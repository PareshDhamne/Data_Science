# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:48:15 2023

@author: Hp
"""

#Tokenization
txt='Welcome to the new year 2023'
x=txt.split()
x

#imports

#removing special charaters
import re
def remove_special_charaters(text):
    #define the aptterm to keep
    pat=r'[^a-zA-Z0-9.,!?/:;\"\'\s]'
    return re.sub(pat, '',text)

#call function
remove_special_charaters('hello @ good morning! %$#@?')

########################################################
#Removing Numbers

def remove_numbers(text):
    #define the aptterm to keep
    pat=r'[^a-zA-Z.,!?/:;\"\'\s]'
    return re.sub(pat, '',text)
remove_numbers("Hello 337")

############################################

txt='Welcome:to the, new year;2023!'
import re
x=re.split(r'(?:,|;|\s)\s*',txt)
x

######################################
#removing punctuation
#imports

import string #function to remove punctuation
def remov_pun(text):
    text= ''.join([c for c in text if c not in string.pun])
    return text#call function
remov_pun('Article:@first sentence dome')
