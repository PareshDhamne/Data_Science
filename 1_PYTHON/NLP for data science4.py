# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:55:17 2023

@author: Hp
"""

#Normalizing unicode text to standard representation
#You'are working with unicode strings but neef to make sure
#that all of thr strings have
#the same underlying representation.
s1 ='Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
s1
s2
s1==s2
########################
#normalization using NFC
import unicodedata
t1 = unicodedata.normalize('NFC',s1)
t2= unicodedata.normalize('NFC',s2)
t1 == t2
####################################
#normalization using NFD
t3 = unicodedata.normalize('NFD',s1)
t4= unicodedata.normalize('NFD',s2)
t3== t4
################################

print(ascii(t3))
print(ascii(t1))
############################

t1 =unicodedata.normalize('NFD',s1)
''.join(c for c in t1 if not unicodedata.combining(c))
################################################

#working with Unicode Characterds in regular expressions
import re
num = re.compile('\d+')
#ascii digits
num.match('123')

######################################
#it's also important to be aware of special cases.
pat=re.compile('stra\u00dfe',re.IGNORECASE)
s ='straße'
num.match(s)
pat.match(s)
s.upper()

###############################
#whitespace stripping(striping unwanted characters from string)
s='     hello world\n'
s.strip()
############################
s='     hello world   \n'
s.lstrip()
###########################3
s='     hello world   \n'
s.rstrip()

#######################
#character stripping
t ='------helllo======'
t.strip('-=') #it will be reomove both -and =
t ='------helllo======'
t.lstrip('-') #it will be remove - and keep = wtih output
t ='------helllo======'
t.rstrip('=') #it will be remove = and keep - wtih output
##################################
s=' hello world     \n'
s=s.strip()
s
s.replace(' ','')

import re
re.sub('s+',' ',s)
###############################

s = 'pýtĥöñ\fis\tawesome\r\n'
s
#the first step is clean up the whitespace.
remap={
       ord('\t'):' ',
       ord('\f'):' ',
       ord('\r'):None #deleted
       }
a=s.translate(remap)
a

#one more technique to remove combining characters:
import unicodedata
import sys
cmb_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b=unicodedata.normalize('NFD',a)
b
b.translate(cmb_chrs)
################################################
#another way fro removing characters is encode and decode
a='pýtĥöñ is awesome\n'
b=unicodedata.normalize('NFD',a)
b.encode('ascii','ignore').decode('ascii')
##############################################
#Aligning the text string
text='Hello World'
text.ljust(20)
text='Hello World'
text.rjust(20)
text='Hello World'
text.center(20)
###############################################
#filling character in empty space
text='Hello World'
text.rjust(20,'=')

text='Hello World'
text.center(20,'=')

text='Hello World'
text.ljust(20,'*')
########################################
text='Hello World'
#> text will be shifted to the right hand side
format(text,'>20')
#< shifted to the left hand side
format(text,'<20')
#^ shifted to the both side
format(text,'^20')
###################################
#shifting with symbols
text='Hello World'
format(text,'=>20')
#< shifted to the left hand side
format(text,'*<20')
#^ shifted to the both side
format(text,'*^20')
##################################

'{:>10s} {:>10s}'.format('Hello','World')
##################################
x=1.2345
format(x,'>10')
x

format(x,'^10.2f')
#######################################
#for joining the parts in the given list
parts=['Is','Chicago','Not','Chicao?']
' '.join(parts)

'Is Chicago Not Chicao?'
#seperated by the commas
','.join(parts)

#without any space
''.join(parts)
############################################

#if you join  very feww strings then you can use + operator

a='Is Chicago'
b='Not Chicago'
a + ' ' + b
############################################
#by using .format method
print('{} {}'.format(a,b))

print(a+' '+b)
###################################
'''
if you are not giving any concatination between two strings it will directly join two strings without any spaceing
'''
a='Hello' 'World'
a

a='Hello'' ''World'
a
########################

#Interpolating Variables in Strings
S='{name} has {n} messages.'
S.format(name='Guido',n=37)
############################3

S='{name} has {n} messages.'
name='Guido'
n=37
S.format_map(vars())
###############################

S="Look into my eyes, look into my eyes, the eyes, the eyes,\
 the eyes, not around the eyes, don't look arounf the eyes,\
 look into my eyes, you're under."
import textwrap
print(textwrap.fill(S,10))
##############################

print(textwrap.fill(S,40,initial_indent=' '))
####################################
print(textwrap.fill(S,40,subsequent_indent=' '))
######################################