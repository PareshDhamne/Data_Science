# -*- coding: utf-8 -*-
"""
Created on Tue May  2 08:23:15 2023

@author: Hp
"""

#list data frames list comptesion dictio ary coprension and pandas and lambda
#what is pandas dataframe?
#how install pandas
#go to anaconda navigator go to environment click on base arrow and open terminal and type pip install pandas
import pandas as pd
pd.__version__
################################################
#create using constructor
#create pandas dataframe from list
import pandas as pd
technologies=[["spark",20000,"30days"],
              ["pandas",20000,"40days"]
              ]
df=pd.DataFrame(technologies)
print(df)
######################################
column_names=["courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
#####################################
df.dtypes
########################################################
types=[{'Courses':str,'Fee':float,'Duration':str}]
df.dtypes
##################################################
#create Dataframe from dictionaries
technologies={
    'courses':["spark","pyspark","Hadoop"],
    'Fee':[20000,25000,26000],
    'Duration':['30days','40days','50days'],
    'Discount':[1000,2300,1500]
    }
df=pd.DataFrame(technologies)
df
#########################################
#convert dataframe to csv
#stored the file in working diritory
df.to_csv('data_file.csv')
df.to_csv('D:/PARESH1_python/data_file.csv')
########################################
#create dataframe from csv file
df=pd.read_csv('data_file.csv')

import pandas as pd

df1 = pd.read_csv('D:/PARESH1_python/data_file.csv')
df1

df
######################################
#pandas dataframe basic operations
#create dataframe with none null to work with examples

import pandas as pd
import numpy as np
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,np.nan],
    'Duration':['30days','40days','50days','40days','20days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
row_labels = ['r0','r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies, index = row_labels)
df
#####################################
#EDA exploratory data analysis
#dataframe properties
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes
####################################
#Accessing one column contents
df['Discount']
#accessing two column and more use double square bracket
df[['Fee','courses']]
#select certain rows and assign it to another dataframe
df2=df[3:] #here 3 represent rows and : represent columns
df2
df3=df[:2]
df3
################################

#accessing cerain cell from column 'Duration'
df['Duration'][2]

#subtracting spcific value from column
df['Fee']=df['Fee']-1 
df['Fee']

#pandas to manipulate dataframe
#describe dataframe
#describe dataframe for all numberic columns
df.describe()
#it will show 5 number summary
########################################

#rename() -renames pandas dataframe columns
df=pd.DataFrame(technologies,index=row_labels)
#assign new header by setting new column names
df.columns=['A','B','C','D']
df

#rename columns using rename() method
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2=df.rename({'A':'C1','B':'C2'},axis=1) #axis=1 for columns and axis=0 for rows
df2=df.rename({'C':'C3','D':'C4'},axis='columns')
df2=df.rename(columns={'A':'C1','B':'C2'})
###############################################





#ASSIGNMENT
import pandas as pd
df = pd.read_csv('D:/PARESH1_python/bank_data.csv')
df
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes

#Accessing one column contents
df['balance']
df['age']

##Accessing two columns contents
df[['loan','duration','pdays']]
df[['balance','age']]

#select certain rows and assign it to another dataframe
df1=df[5:]
df1

df2=df[20000:]
df2

df1=df[:12]
df1

df2=df[:2]
df2

#accessing certain cell from column
df['duration'][20000]
df['age'][3]
df['balance'][1]

#Describe DataFrame
df.describe()

#rename() – Renames pandas DataFrame columns
df.columns=['1','2','3','4','5','6','7','8','9','10','11','12',
            '12','13','14','15','16','17','18','19','20','21','22',
            '23','24','25','26','27','28','29','30','31']
df

# Rename Column Names using rename() method
df2=df.rename({'1':'A','2':'B','3':'C','4':'D','5':'E'},axis=1) 
df2
df2=df.rename({'6':'F','7':'G','8':'H'},axis='columns')
df2
df2=df.rename(columns={'1':'A','2':'B','3':'G','4':'H'})
df2
############################################################

import pandas as pd
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi","Hindi"],
    'Fee':[20000,25000,26000,50000,23000,21000,200],
    'Duration':['30days','40days','50days','40days','20days','10days','5days'],
    'Discount':[1000,2300,1500,1000,200,100,10]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

#converting all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)

#change all columns to same type
df=df.astype(str)
print(df.dtypes)

#change type for one or more multiple columns
df=df.astype({"Fee":int,"Discount":int})
print(df.dtypes)

#convert data type for all columns in a list
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes

cols=['courses','Duration']
df[cols]=df[cols].astype('string')
df.dtypes
####################################################
#ignores error
df=df.astype({"courses":int},errors='ignore')
df.dtypes

#Generates error
df=df.astype({"courses":int},errors='raise')
df.dtypes

#convert feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df['Fee']=pd.to_numeric(df['Fee'])
df.dtypes
df['Discount']=pd.to_numeric(df['Fee'])
df.dtypes
###############################################

#Drop DataFrame Rows and Columns
row_labels = ['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
df1=df.drop(['r1','r5'])
df1
...
#Delete row by position
df1=df.drop(df.index[[1,3]])
df1

#Delete row by index range
df1=df.drop(df.index[2:])
df1

#When you have default indexs for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1

df=pd.DataFrame(technologies)
df1=df.drop([0,3]) #it will delete row0 and row3
df1=df.drop(range(0,2)) #it will delete 0 and 1
df1
############################################

import pandas as pd
technologies=({
    'courses':['spark','pyspark','Hadoop','python','pandas','oracle','Java'],
    'Fee':[20000,10000,50000,1000,200,300,400],
    'Duration':['30days','40days','25days','10days','80days','45days','37days']
    })
df=pd.DataFrame(technologies)
df






#Assignment
import pandas as pd
df=pd.read_csv('D:/PARESH1_python/AutoInsurance.csv')
df

#for rows and columns
df.shape
#for size of file
df.size
#for display of columns
df.columns
#index
df.index
#for datatypes
df.dtypes

#Accessing one column contents
df['Customer']

##Accessing two columns contents
df3=df[['State','Coverage','Education','Income']]
df3

#select certain rows and assign it to another dataframe
df1=df[7000:]
df1

df2=df[:12]
df2

#accessing certain cell from column
df['Customer'][2]
df['State'][11]

#Describe DataFrame
df.describe()

#rename() – Renames pandas DataFrame columns
df.columns=['1','2','3','4','5','6','7','8','9','10','11','12',
            '12','13','14','15','16','17','18','19','20','21','22',
            '23']
df

# Rename Column Names using rename() method
df1=df.rename({'1':'A','2':'B'},axis=1) 
df1
df2=df.rename({'3':'C','4':'D'},axis='columns')
df2
df3=df.rename(columns={'1':'A','2':'B','3':'G','4':'H'})
df3

#Drop DataFrame Rows and Columns
df2=df[:12]
df2
# Drop rows by labels
df1=df2.drop([0,11])
df1

# Delete Rows by position
df1=df2.drop(df.index[[1,3,5]])
df1

df3=df.drop(df.index[1500:])
df3

# Delete Rows by Index Range
df3=df.drop(df.index[1500:])
df3

#for default
df1=df.drop(0)
df1

#Select Rows by Index
df2=df[100:500]
df2
###################################################################

import pandas as pd
technologies=({
    'courses':['spark','pyspark','Hadoop','python','pandas','oracle','Java'],
    'Fee':[20000,10000,50000,1000,200,300,400],
    'Duration':['30days','40days','25days','10days','80days','45days','37days']
    })
df=pd.DataFrame(technologies)
df

#Drop column by name
#Drop 'Fee' column
df2=df.drop(['Fee'],axis=1)
print(df2)

#Explictily using parameter name 'labels'
df2=df.drop(labels=["Fee"],axis=1)
df2

#Alternativly you can also use columns insted of labels
df2=df.drop(columns=["Fee"],axis=1)
df2

#Drop column by index
print(df.drop(df.columns[1],axis=1))

df=pd.DataFrame(technologies)
#using inplace=True
df.drop(df.columns[[2]],axis=1,inplace=True)
df
df.drop(df.columns[2],axis=1,inplace=True)
df

#####################################
df=pd.DataFrame(technologies)
#Drop two or more columns by level name
df2=df.drop(["courses","Fee"],axis=1)
df2

#Drop two or more columns by index
df=pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]],axis=1)
df2

#Drop columns from list of columns
df=pd.DataFrame(technologies)
lisCol=["courses","Fee"]
df2=df.drop(lisCol,axis=1)
df2
######################################
###################################

#pandas Select rows by index(position/label)
#for index=iloc and use square bracket[ ]
#for labels=loc and use square bracket[ ]
import pandas as pd
import numpy as np
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,np.nan],
    'Duration':['30days','40days','50days','40days','20days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
row_labels = ['r0','r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies, index = row_labels)
df

#df.iloc[startrow:endrow,startcolmn:endcolmn]
df = pd.DataFrame(technologies, index = row_labels)
#below are quick examples
df2=df.iloc[:,0:2]
df2

df3=df.iloc[1:5,0:2]
df3

#this line uses the slicing operator to get DataFrame
#item by index
#the first slice[:] indicates to return all rows
#the secod slce specifices that only column
df2=df.iloc[0:2,:]
df2

#slicing specific rows and columns using iloc attribute
df3=df.iloc[1:4,1:3]
df3

#select rows by integer index
df2=df.iloc[2]
df2

#select rows by index list
df2=df.iloc[[2,3,4]]
df2

#select row by integer index range
df2=df.iloc[1:3]

#Select first row
df2=df.iloc[:1]

#for first 3
df2=df.iloc[:3]

#select last row
df2=df.iloc[-1:]
df2
df2=df.iloc[-3:]
df2

#select alternativ rows
df2=df.iloc[::2]
df2

#select row by index label
df = pd.DataFrame(technologies, index = row_labels)
df2=df.loc['r2']
df2
#select rows by index label
df2=df.loc[['r2','r3','r5']]
df2

#select rows by label index
df2=df.loc['r1':'r5']
df2

#select alternative label index
df2=df.loc['r1':'r5':2]
df2
##############################################

#select multiple columns
df2=df.loc[:,["courses","Fee","Duration"]]
df2

#select random columns
df2=df.loc[:,["courses","Fee","Discount"]]
df2

#select columns between two cloumns
df2=df.loc[:,'Fee':'Discount']
df2

#select column by range
df2=df.loc[:,'Duration':]
df2

#All the columns upto "Duration"
df2=df.loc[:,:"Duration"]
df2

#select every alternative colmn
df2=df.loc[:,::2]
df2
###########################################

#Pandas.DataFrame.query() by example
#query all rows with courses equal 'Spark'
df2=df.query("courses=='spark'")
df2
###########################################

#not equals condition
df2=df.query("courses != 'spark'")
df2
######################################
#pandas add column to data frame
import pandas as pd

