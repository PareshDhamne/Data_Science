# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:23:15 2023

@author: Hp
"""

#series is used model one dimensional data
#similar to list in python but not list
#series object also have a few more bits
#of data, including an #index and a name
import pandas as pd
songs2=pd.Series([145,142,38,13],name='counts')
songs2.index

#the index can be string based as well,
#in which case pandas indicates
#that the datatype for  the index is object(not string)

song3=pd.Series([145,142,38,13],name='counts',
                index=['paul','john','kk','arjit'])
song3.index
song3

#THE NAN VALUE
#THIS VALUE STANDS FOR NOT A NUMBER,
#AND IS USUALLY IGORED IN ARITHMETIC
#OPERATIONS.{SIMILAR TO NULL IN SQL}
#IF YOU LOAD DATA FROM A CSV FILE
#an empty valur for an otherwise
#NUMERIC COLUMN WILL BECOME NAN

import pandas as pd


#none , nan , and null are synous
#the series object behavies similar to numpy array
import pandas as pd
songs1=pd.Series([145,142,38,13])
songs1[2]
songs1.mean()


#the pandas series data structure provides
george=pd.Series([10,7,1,22],
                 index=['1998','1969','1970','1970'],
                 name='George Songs')
george

##########################################
#reading
#to read or select the data from a series
george['1998']
george['1970']

#we can iterate over data in a series
#as well. Wehn iterating over a series
for item in george:
    print(item)
##########################################
#updating value in series

george['1998']=70
george['1998']

#Deletion
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

#########################################
#cONVERT TYPES
#string use.astype(str)
##numeric use pd.to_numeric
#integer use.astype(int),
#note that this will fail with Nan
import pandas as pd
songs_66 = pd.Series([3,None,11,9],
                     index=['paul','john','kk','arjit'],
                     name='Counts')

pd.to_numeric(songs_66.apply(str))
#it shows error

#use this
pd.to_numeric(songs_66.apply(str),errors='coerce')

#Dealing with None
songs_66.fillna(-1)

#Nan values can be dropped from the series using .dropna
songs_66.dropna()
##################################################

#APPEND, COMBINING, AND JOINING TWO SERIES
songs_69=pd.Series([7,16,21,39],
                   index=['Ram','Sham','Ghansham','Krishna'],
                   name='Counts')

#To concatenate two series together, simply use the .append method
songs=songs_66.append(songs_69)
######################################

#plotting two series
import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot()
plt.legend()
###################################

fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r',alpha=.5)
plt.legend()
###################################
import numpy as np
data=pd.Series(np.random.randn(500),
name='500 random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
##################################


