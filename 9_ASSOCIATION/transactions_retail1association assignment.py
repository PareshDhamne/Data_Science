# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:56:33 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    Utilizing association rules, the mobile phone manufacturing company can recommend phone models 
    frequently associated with each other, optimizing marketing strategies to maximize sales while
    minimizing costs. By analyzing previous model sales data, the company can tailor targeted marketing 
    approaches, improving customer satisfaction and driving business growth.

Business Problem:
    1.1.	What is the business objective?
    - Maximize:Maximize customer footfall by arranging products on shelves in a way that attracts customers and promotes cross-selling.
  
    - Minimize:Minimize the occurrence of stockouts by optimizing inventory based on popular product associations.
  
    -constraints:Ensure that the recommended product placement strategies fit within the available shelf space.
"""

from mlxtend.frequent_patterns import apriori,association_rules

#here we are going to use MYPHONE data 
#here function called open() is used
#create an empty list
with open("D:/ASSOCIATION/transactions_retail1.csv") as f:transactions_retail1=f.read()
#it will read all data from transactions_retail1.csv file 
################################################################################

#splitting the data into separate transaction using separator
#we can use nrw line character "\n"

transactions_retail1=transactions_retail1.split("\n")
transactions_retail1
#it will split all the data into size 557042
#and data type is string. Each data is seperateed by comma

#now we will have to seperate out each item form each transaction data
#for that create ne empty list
transactions_retail1_list=[]
for i in transactions_retail1:
    transactions_retail1_list.append(i.split(","))
#split function will seperate each item from each list, whenever it will find 
#in order to generate association rules, we can directly use transactions_retail1_list 
#Now let us seperate out each item from the transactions_retail1_list

all_transactions_retail1_list=[i for item in transactions_retail1_list for i in item]
all_transactions_retail1_list
#we will get all the items occured in data
#we will get 3348059 items in various transaction data
##################################################################################

#Now let us count the frequency of each item
#we will import collections package which has Counter frunction which will
from collections import Counter
item_frequencies=Counter(all_transactions_retail1_list)
item_frequencies
#it will display the output in the format of key and values in dictionary format

#we want to access values and sort baseed on the count theat occured in it. 
#it will show the count of each item  in every transaction data
#Now let us sort these frequencies in ascending order 
item_frequencies=sorted(item_frequencies.items(),key=lambda x:x[1])
item_frequencies
#When we execute this, item frequencies will be in sorted form , in the form of item name with count 

#Let us seperate out items and their count
items=list(reversed([i[0] for i in item_frequencies]))
items
#This is list comprehension forn each item in item frequencies access the key 
#here you will set items list
frequencies=list(reversed([i[1] for i in item_frequencies]))
#here you will get count of purchase of each item 
######################################################################################

#Now let us plot bar graph of item frequencies 
import matplotlib.pyplot as plt
#there we are taking frequencies from zero to 14 you can try 0-15 or anuy other
plt.bar(height=frequencies[0:14],x=list(range(0,14)))
plt.xticks(list(range(0,14)),items[0:14])
plt.xticks(rotation=90)

#plt.xtics you can specify a rotation for the tick
#labels in degrees or with keywords

plt.xlabel("items")
plt.ylabel("count")
plt.show 
#######################################################################################

import pandas as pd
#now let us try to establish association rule mining 
#we have transactions_retail1 list in the list format, we need to convert it in dataframe
transactions_retail1_series=pd.DataFrame(pd.Series(transactions_retail1_list))
transactions_retail1_series
#now we will get datarfreame odf size 557042x1 size colums
#comprises of multiple items

#last rows is empty, let us first delete it
transactions_retail1_series=transactions_retail1_series.iloc[:557041,:]
transactions_retail1_series

#we have taken ros from 0 to 557041 and column 0 to all
#transactions_retail1 series has column  having name o let us rename transactions
transactions_retail1_series.columns=['Transactions']

#now we will have to apply 1n hot encoder before that in 
#one column there are various items separated by
# let us seprated with '*"
x=transactions_retail1_series['Transactions'].str.join(sep='*')

#check the x in variables explorer which has * sepreated rather the ','
x=x.str.get_dummies(sep='*')
x
#we will get one hot encoded data frame of size 557041x
#This is our input data to apply to apriori algorithm, it will generate !169 rules, min support values 
#is 0.0075 (it must be between 0 to 1), 

frequent_itemsets=apriori(x,min_support=0.0075,max_len=4,use_colnames=True)
#you will get support values for 1,2,3 an d 4 max items

#let us sort these support values 
frequent_itemsets.sort_values('support',ascending=False,inplace=True)
frequent_itemsets
#Support values will be sorted in descending order 

#we will generate  association rules, This association rule will calculate all the matrix of each and every combination 
rules=association_rules(frequent_itemsets,metric='lift',min_threshold=1)
#this generate associatin rules of size 362x10 columns 
#comprises of antescends, consequences 
rules.head(20)
rules.sort_values('lift',ascending=False).head(10)
###############################################################################
'''
Benifits to the client:
    By leveraging association rules, the mobile phone manufacturing company can strategically position 
    products to maximize customer engagement, minimize stockouts, and optimize inventory, thus enhancing
    customer satisfaction while driving business growth.
'''
##############################################################################
