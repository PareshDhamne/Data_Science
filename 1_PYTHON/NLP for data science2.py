# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:31:59 2023

@author: Hp
"""
import re
line='asdf fjdk;afed fjek,asdf,foo'
re.split(r'(?:,|;|\s)\s*',line)
########################################

pattern=r'(?:,|;|\s)\s*'
x=re.split(pattern,txt)
print(x)
##############################################

#matching text at the time to start or rnd of string
filename='span.txt'
filename.endswith('.txt')
######################################

area_name='6 the lane west Andheri1'
area_name.endswith('west Andheri1')

#####################################

choises=('http:','ftp:')
url='http://www.python.org'
url.startswith(choises)

#######################################3

#slicing a string
#If a S is a string
#S is a string, the expression S[start:stop:step]

S='ABCDEFGHI'
print(S[2:7])
##################################

#slice with negative indices
S='ABCDEFGHI'
print(S[-7:-2])
print(S[2:-5])

###################################
#specify the steps 
S='ABCDEFGHI'
print(S[2:7:2])
S[6:1:-2]

#slicing of begning and end
S='ABCDEFGHI'
S[:3]
S[6:]
###########################
#reversing a string
S[::-1]
#########################
#similar operations can be done with slices
filename='span.txt'
filename[-4:]=='.txt'
###########################
url='http://www.python.org'
url[:5]=='http:' or url[:6]=='https' or url[:4]=='ftp:'
##################################
from fnmatch import fnmatch, fnmatchcase
names=['Dat1.csv','Dat2.csv','config.ini','foo.csv']
[name for name in names if fnmatch(name, 'Dat*.csv')]
###################################
from fnmatch import fnmatch,fnmatchcase
names=['Andheri East','Parle East','Dadar West']
[name for name in names if fnmatch(name,'*East')]
####################################
from fnmatch import fnmatch,fnmatchcase
addresses=[
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
    ]
[address for address in addresses if fnmatch(address,'*ST')]
########################################
text='yeah, but no, but yeah, but no, but yeah'
#Exact match
text=='yeah'

#match at starts or end
text.startswith('yeah')
text.endswith('no')

#search for the loaction of the first occurrence that index will be shown
text.find('no')
###########################################
text1='11/27/2012'
text2='Nov 27, 2012'
import re 
#simple matching:\d+ means match one or more digit
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
#yes
if re.match(r'\d+/\d+/d+', text2):
    print('yes')
else:
    print('no')
############################################
text='33-22-5555'
if re.match(r'\d{2}-\d{2}-\d{4}', text):
    print('yes')
else:
    print('no')
###################################

#ASSIGNMENT
text="This is Artificial Intelligence Era"
a=text.split()
a
###############################################
import re
text="India : has great history: in 2023 india is leading to its glories future!"    
x=re.split(r'(?:,|;|\s)\s*',text)
print(x)
###################################################
#matching text at the sta and end of list
text='Rama went to haridwar to get gangajal'
text.startswith('gangajal')
text.endswith('gangajal')
################################################
text='Rama went to haridwar to get gangajal'
x=('Rama','gangajal','haridwar')
text.startswith(text)
text.endswith(text)
###########################################
text='I like Mango'
text[7:]=='Mango'
text[-4:]=='Mango'
#################################
text='I had been visited Pune on 11/05/2023'
text[-10:]
import re 
re.findall(r'\d+/\d+/\d+', text)
    print('11/05/2023')
else:
    print('no')
######################################

#searching and replacing text
text='yeah, but no, but yeah, but no, but yeah'
text.replace('yeah','yup')
#############################

text='Today is 17/05/2023 and our exam will start on 02/07/2023'
re.sub(r'(\d+)/(\d+)/(\d+)',r'(\3-\1-\2)',text)
##################################

datepan=re.compile(r'(\d+)/(\d+)/(\d+)')
datepan.sub(r'\3-\1-\2',text)
##################################

newtext,n=datepan.subn(r'\3-\1-\2',text)
newtext,n
print(n)
##################################
#searching and replacing case sensitive text
text='Upper PYTHON, lower python, Mixed Python'
re.findall('python',text, flags=re.IGNORECASE)
re.sub('python','snake',text,flags=re.IGNORECASE)
###################################