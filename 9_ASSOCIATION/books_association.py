# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:27:49 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    Kitabi Duniya, a famous book store in India, which was established before Independence, the growth 
    of the company was incremental year by year, but due to online selling of books and wide spread 
    Internet access its annual growth started to collapse, seeing sharp downfalls, you as a Data Scientist 
    help this heritage book store gain its popularity back and increase footfall of customers and provide
    ways the business can improve exponentially, apply Association RuleAlgorithm, explain the rules, and 
    visualize the graphs for clear understanding of solution.

1.	Business Problem:
    1.1.	What is the business objective?
    - Maximize:Increase sales for Kitabi Duniya by promoting book associations to enhance the overall customer shopping experience. 
    - Minimize:Minimize operational costs associated with implementing new strategies
    - Constraints:Customer satisfaction.


Datadictionary:
    
 1.ChildBks containing Children's books category is nominal data.  
 2.YouthBks containing Youth books category is nominal data. 
 3.CookBks  containing cookbooks category   is nominal data. 
 4.RefBks containing Reference books category is nominal data. 
 5.ArtBks containing Art books category  is nominal data. 
 6.GeogBks containing Geography books category is nominal data. 
 8.ItalCooks containing Italian Cookbooks category  is nominal data.   
 9.ItalAtlas containing Italian Atlases category  is nominal data.
 10.ItalArt  containing Italian Art books category is nominal data.
 11.Florence containing Possibly a location or specific book related to Florence is nominal data.    
              
book.csv is file in which there is different types ogf books data is associated
like childbooks,youthbooks,cookingbooks,doltybooks,reference books,art books,geogrophy books,italian books and florence

"""

from mlxtend.frequent_patterns import apriori,association_rules

#here we are going to use book data 
#here function called open() is used
#create an empty list
with open("D:/ASSOCIATION/book.csv") as f:book=f.read()
#it will read all data from book.csv file 
###########################################################################
#splitting the data into separate books using separator
#we can use nrw line character "\n"

book=book.split("\n")
book
#it will split all the data into size 2002
#and data type is string. Each data is seperateed by comma
############################################################################
#now we will have to seperate out each item form each book
#for that create ne empty list
book_list = []
for i in book:
    book_list.append(i.split(","))
#split function will seperate each item from each list, whenever it will find 
#in order to generate association rules, we can directly use book_list 
#Now let us seperate out each item from the book_list

all_book_list=[i for item in book_list for i in item]
all_book_list
#we will get all the items occured in all books
#we will get 22012 items in various books
 ################################################################################

#Now let us count the frequency of each item
#we will import collections package which has Counter frunction which will 
from collections import Counter 
item_frequencies = Counter (all_book_list)
item_frequencies
#it will display the output in the format of key and values in dictionary format

#we want to access values and sort baseed on the count theat occured in it. 
#it will show the count of each item purchased in every book transaction
#Now let us sort these frequencies in ascending order 
item_frequencies=sorted(item_frequencies.items(),key=lambda x:x[1])
item_frequencies
#When we execute this, item frequencies will be in sorted form , in the form of item name with count 
####################################################################################

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
#here we are taking frequencies from zero to 3 only
plt.bar(height=frequencies[0:3],x=list(range(0,3)))
plt.xticks(list(range(0,3)),items[0:3])
plt.xticks(rotation=90)
#plt.xticks, You can specify a rotation for the tick 
#labels in degrees or with keywords 
plt.xlabel("items") 
plt.ylabel("count")
plt.show()
##########################################################################################

import pandas as pd
#now let us try to establish association rule mining 
#we have book list in the list format, we need to convert it in dataframe 
book_series = pd.DataFrame(pd.Series(book_list))
book_series
#Now we will get dataframe of size 2002x1 size, columns comprises of multiple items 
# the last row of the dataframe is empty so we will remove it
book_series = book_series.iloc[:2001,:] 
book_series
##############################################################################################

#we have taken rows from 0 to 2000  and columns 0 to all 
#book series has column having name 0, let us rename as transactions
book_series.columns=["Transactions"]

#Now we will have to apply 1-hot encoding, before that in one column there are various items seperated by ','
#let us seperate it with '*'
x=book_series["Transactions"].str.join(sep='*')

#check the x in variable explorer which has * seperator rather that ','
x=x.str.get_dummies(sep='*')

#we will get one hot encoded data frame of size 2001x12
#This is our input data to apply to apriori algorithm, it will generate !169 rules, min support values 
#is 0.0075 (it must be between 0 to 1),
####################################################################################

frequent_itemsets = apriori(x,min_support=0.0075,max_len=4,use_colnames=True)
#you will get support values for 1,2,3 and 4 max items 

#let us sort these support values 
frequent_itemsets.sort_values('support',ascending=False,inplace=True)
frequent_itemsets
#Support values will be sorted in descending order 
###################################################################################
#we will generate  association rules, This association rule will calculate all the matrix of each and every combination 
rules=association_rules(frequent_itemsets,metric='lift',min_threshold=1)
#this generate associatin rules of size 1198x9 columns 
#comprises of antescends, consequences 
rules.head(20)
rules.sort_values('lift',ascending=False).head(10)
###############################################################################

'''
Benifits to the client:
    Utilize association rules to recommend related books, optimize inventory, and personalize marketing, 
    enhancing Kitabi Duniya's customer experience and increasing sales while minimizing operational costs.
'''
##############################################################################










