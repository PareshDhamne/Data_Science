# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:19:11 2023

@author: Hp
"""
from mlxtend.frequent_patterns import apriori,association_rules

#here we are going to use transactional data wherein size of each row is not
#we can not use pandas to load this unstructured data
#here function called open() is used
#create an empty list
with open("D:/Datasets/groceries.csv") as f:groceries=f.read()
#splitting the data into separate transactions using separator, it is comma
#we can use nrw line character "\n"

groceries=groceries.split("\n")
#earlier groceries datastructure was in string format, now it willchange to
#9836 each item is comma seperatead
#our main aim is to calculate #A, #c
#we will have to seperate out each item from each transaction
groceries_list=[]
for i in groceries:
    groceries_list.append(i.split(","))
#split function will separate each item from each list, wherever it will from
#in orderto generate association rules, you can directly use groceries_list
#now let us seperate out each item from the groceries list
all_groceries_list=[i for item in groceries_list for i in item]
#you will get all the items occured in all transactons
#we will get 43368 items in various transactions

#now let us count the frequency of each item
#we will import collections package which has counter function which will be

from collections import Counter
item_frequencies=Counter(all_groceries_list)

#item_frequencies is basically dictionary having x[0] as key and x[1]=values
#we want to access values and sort based on the count that occured in it
#it willl be show the count of each item purchase in every transaction
#now let us sort theser frequencies in ascending order

#now let us sort these frequencies in ascending order
item_frequencies=sorted(item_frequencies.items(),key=lambda x:x[1])
#when we ec=xexcute this, item frequencies will be in sorted form,
#in the form of tuple
#item name with ccount
#let us separater out items and their count
items=list(reversed([i[0] for i in item_frequencies]))
#this is list comprehencsion for esch item in item frequencies access the key
#there you will get item set
frequencies=list(reversed([i[1] for i in item_frequencies]))
#tehre you will get count of purchase of each item

#now let us plot graph of item frequencies
import matplotlib.pyplot as plt
#there we are taking frequencies from zero to 11 you can try 0-15 or anuy other
plt.bar(height=frequencies[0:11],x=list(range(0,11)))
plt.xtics(list(range(0,11)),items[0:11])

#plt.xtics you can specify a rotation for the tick
#labels in degrees or with keywords

plt.xlabel("items")
plt.ylabel("count")
plt.show 

import pandas as pd
#now let us try to esatblish association rul mining
#we have groceries list in the lsit format, need to convert it into datafrsme
groceries_series=pd.DataFrame(pd.Series(groceries_list))
#now we will get datarfreame odf size 9836x1 size colums
#comprises of multiple items
#we had extra rows created, check the grocerie_series
#last rows is empty, let us first delete it
groceries_series=groceries_series.iloc[:9835,:]
groceries_series

#we have taken ros from 0 to 9834 and column 0 to all
#groceries series has column  having name o let us rename transactions
groceries_series.columns=['Transactions']
#now we will have to apply 1n hot encoder before that in 
#one column there are various items separated by
# let us seprated with '*"
x=groceries_series['Transactions'].str.join(sep='*')
#check the x in variables explorer which has * sepreated rather the ','
x=x.str.get_dummies(sep='*')
#you will get one hot encoded dataframe os size 9835x169
#this is our input data to aply apriori algotherem
#it will generate 169 rules suppose value
#is 0.075
#you can give any number but must be betwenn 0 to1 
frequent_itemsets=apriori(x,min_support=0.0075,max_len=4,use_colnames=True)
#you will get support values for 1,2,3 an d 4 max items
frequent_itemsets.sort_values('support',ascending=False,inplace=True)
#support values will be sorted in ascending ordwe
#even eda was also have the same trend in eda there was count
#and here itis support values
#we will generate association rules this association
#rule will calculate all the matrix
#of each and every combiation
rules=association_rules(frequent_itemsets,metric='lift',min_threshold=1)
# This generate association rule of size 1198x9 columns
# comprises of antescends,consequences

rules.head(20)
rules.sort_values('lift',ascending=False).head(10)
