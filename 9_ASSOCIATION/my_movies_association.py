# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:29:14 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    A film distribution company wants to target audience based on their likes and dislikes, 
    you as a Chief Data Scientist Analyze the data and come up with different rules of movie 
    list so that the business objective is achieved.
    

1.	Business Problem:
    1.1.	What is the business objective?
    - Maximize:Increase the number of audience by promoting movie associations to enhance the overall movie experience. 
    - Minimize:Dislikes from audience

Business Constraints:
    - Constraints:audience satisfaction.

DataFrame:
my_movies.csv is file in which there are some movies given
like Sixth Sense,Gladiator,LOTR1,Harry Potter1,Patriot,LOTR2,Harry Potter2,LOTR,Braveheart,Green Mile
All are categorical(nominal) data 1: liked, 0: not liked

"""

from mlxtend.frequent_patterns import apriori,association_rules

#here we are going to use book data 
#here function called open() is used
#create an empty list
with open("D:/ASSOCIATION/my_movies.csv") as f:my_movies=f.read()
#it will read all data from my_movies.csv file 
##########################################################################

#splitting the data into separate books using separator
#we can use nrw line character "\n"

my_movies=my_movies.split("\n")
my_movies
#it will split all the data into size 12
#and data type is string. Each data is seperateed by comma

#now we will have to seperate out each item form each movie
#for that create ne empty list
my_movies_list = []
for i in my_movies:
    my_movies_list.append(i.split(","))
#split function will seperate each item from each list, whenever it will find 
#in order to generate association rules, we can directly use my_movies_list 
#Now let us seperate out each item from the my_movies_list

all_my_movies_list=[i for item in my_movies_list for i in item]
all_my_movies_list
#we will get all the items occured in all books
#we will get 111 items in various books
################################################################################

#Now let us count the frequency of each item
#we will import collections package which has Counter frunction which will 
from collections import Counter 
item_frequencies = Counter (all_my_movies_list)
item_frequencies
#it will display the output in the format of key and values in dictionary format

#we want to access values and sort baseed on the count theat occured in it. 
#it will show the count of each movie seen by audience
#Now let us sort these frequencies in ascending order 
item_frequencies=sorted(item_frequencies.items(),key=lambda x:x[1])
item_frequencies
#When we execute this, item frequencies will be in sorted form , in the form of item name with count 

#Let us seperate out items and their count 
items = list(reversed([i[0] for i in item_frequencies]))
items
#This is list comprehension forn each item in item frequencies access the key 
#here you will set items list 
frequencies = list(reversed([i[1] for i in item_frequencies]))
#here you will get count of purchase of each item 
####################################################################################

#Now let us plot bar graph of item frequencies 
import matplotlib.pyplot as plt 
#here we are taking frequencies from zero to 4 only
plt.bar(height=frequencies[0:4],x=list(range(0,4)))
plt.xticks(list(range(0,4)),items[0:4])
plt.xticks(rotation=90)
#plt.xticks, You can specify a rotation for the tick 
#labels in degrees or with keywords 
plt.xlabel("items") 
plt.ylabel("count")
plt.show()
#################################################################################

import pandas as pd
#now let us try to establish association rule mining 
#we have my_movies list in the list format, we need to convert it in dataframe 
my_movies_series = pd.DataFrame(pd.Series(my_movies_list))
my_movies_series

#Now we will get dataframe of size 12x1 size, columns comprises of multiple items 
# the last row of the dataframe is empty so we will remove it
my_movies_series = my_movies_series.iloc[:11,:] 
my_movies_series

#we have taken rows from 0 to 10  and columns 0 to all 
#my_movies series has column having name 0, let us rename as transactions
my_movies_series.columns=["Transactions"]

#Now we will have to apply 1-hot encoding, before that in one column there are various items seperated by ','
#let us seperate it with '*'
x=my_movies_series["Transactions"].str.join(sep='*')

#check the x in variable explorer which has * seperator rather that ','
x=x.str.get_dummies(sep='*')

#we will get one hot encoded data frame of size 11x12
#This is our input data to apply to apriori algorithm, it will generate !169 rules, min support values 
#is 0.0075 (it must be between 0 to 1),

frequent_itemsets = apriori(x,min_support=0.0075,max_len=4,use_colnames=True)
#you will get support values for 1,2,3 and 4 max items 

#let us sort these support values 
frequent_itemsets.sort_values('support',ascending=False,inplace=True)
frequent_itemsets
#Support values will be sorted in descending order 

#we will generate  association rules, This association rule will calculate all the matrix of each and every combination 
rules=association_rules(frequent_itemsets,metric='lift',min_threshold=1)
#this generate associatin rules of size 1198x9 columns 
#comprises of antescends, consequences 
rules.head(20)
rules.sort_values('lift',ascending=False).head(10)

###########################################################################
'''
Benifits to the client:
    Leverage association rules derived from movie preferences to recommend movie associations, 
    enhancing audience engagement and satisfaction while minimizing dislikes, thus maximizing audience 
    numbers and achieving business growth for the film distribution company.
'''
###########################################################################









