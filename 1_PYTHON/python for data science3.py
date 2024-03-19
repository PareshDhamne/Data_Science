# -*- coding: utf-8 -*-
"""
Created on Mon May  8 08:16:24 2023

@author: Hp
"""

#pandas apply function to a column
#below are quicl\k examples
#using dataframe.apply() to apply function add column

import pandas as pd
import numpy as np

data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
df

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
########################################

#using apply function single column
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]

#apply to multiple columns
df[['A','B']]=df[['A','B']].apply(add_3)
df

#apply a lambda function to each column
df2=df.apply(lambda x:x+10)
df2

#apply lambda fun to single column
df["A"]=df["A"].apply(lambda x:x-2)
df
###################################
#using pandas.DataFrame.transform() to apply function column
#using DataFrame.transform()
def add_2(x):
    return x+2
df=df.transform(add_2)
df
########################################
#using pandas>dataframe.map() to single column

df['A']=df['A'].map(lambda A: A/2.)
df

####################################

#using numpy function on single column
#using dataframe.apply() and [] operator
import numpy as np
df['A']=df['A'].apply(np.square)
df
#######################################
#using Numpy.square() method
#using numpy.square() and [] operator
df['A']=np.square(df['A'])
df
###############################
#pandas groupby() with examples
import pandas as pd
technologies=({
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi","spark","pyspark","Hadoop","NA"],
    'Fee':[20000,25000,26000,2400,23000,2400,2500,3000,1200,3200],
    'Duration':['30days','40days','50days','40days','20days','10days','30days','10days','9days','45days'],
    'Discount':[1000,2300,1500,1000,200,100,None,1400,1600,0]
    })
df=pd.DataFrame(technologies)
df

#use groupby() to compute sum
df2=df.groupby(['courses']).sum()
df2
##########################################3

#group by multiple columns
df3=df.groupby(['courses','Duration']).sum()
df3
######################################
#add index to the groupby data
#add row index to the group by result
df2=df.groupby(['courses','Duration']).sum().reset_index()
df2
################################
#group by on multiple columns
df2=df.groupby(['courses','Duration']).sum()
df2
###########################
import pandas as pd
import numpy as np
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English"],
    'Fee':[20000,25000,26000,50000,23000],
    'Duration':['30days','40days','50days',None,np.nan],
    'Discount':[1000,2300,1500,1000,200]
    }
df=pd.DataFrame(technologies)
df

df.columns

#get the list of all column names from header
columns_header=list(df.columns.values)
print("The column Header:",columns_header)

#####################################
#using list(df) to get the column headers as a list
column_headers=list(df.columns)
column_headers

#using list(df) to get the list of all column names
column_headers=list(df)
column_headers

#########################################
############################
import pandas as pd
technologies={
    'courses':["spark","pyspark","Hadoop","Python","English","Marathi"],
    'Fee':[20000,25000,26000,50000,23000,24000],
    'Duration':['30days','40days','50days','40days','20days','10days'],
    'Discount':[1000,2300,1500,1000,200,100]
    }
df=pd.DataFrame(technologies)
df

#pandas shuffle Dataframe rows
#shuffle the DataFrame rows and return all rows

df1= df.sample(frac=1)
df1
#######################################

#create a new index starting from zero
df1=df.sample(frac=1).reset_index()
df1
#########################

#Drof shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
df1
################################




#Assignment
import pandas as pd
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
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
######################################
#Accessing one column contents
df['Population']

##Accessing two columns contents
df1=df[['Sales','Education']]
df1
################################
#select certain rows and assign it to another dataframe
df2=df[100:]
df2

#accessing certain cell from column
df['CompPrice'][2]

#Describe DataFrame
df.describe()
######################################
#rename() – Renames pandas DataFrame columns
df.columns=['1','2','3','4','5','6','7','8','9','10','11']
df

# Rename Column Names using rename() method
df3=df.rename({'1':'A','2':'B'},axis=1) 
df3
df4=df.rename({'3':'C','4':'D'},axis='columns')
df4
df5=df.rename(columns={'1':'A','2':'B','3':'G','4':'H'})
df5
###########################################
#Drop DataFrame Rows and Columns
df6=df[:12]
df6
# Drop rows by labels
df7=df.drop([0,11])
df

# Delete Rows by position
df8=df.drop(df.index[[1,3,5]])
df8

df9=df.drop(df.index[50:])
df9

# Delete Rows by Index Range
df10=df.drop(df.index[14:])
df10

#for default
df11=df.drop(0)
df11
#######################################
#Select Rows by Index
df12=df[10:150]
df12

#converting all types to best possible types
df13=df.convert_dtypes()
print(df13.dtypes)

#change all columns to same type
df14=df.astype(str)
print(df14.dtypes)

#change type for one or more multiple columns
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df15=df.astype({"Sales":int,"Education":int})
print(df15.dtypes)

#convert data type for all columns in a list
df.dtypes
cols=['Sales','Age']
df[cols]=df[cols].astype('float')
df.dtypes

#ignores error
df16=df.astype({"Sales":int},errors='ignore')
df16.dtypes

#Generates error
df17=df.astype({"Sales":int},errors='raise')
df17.dtypes
###############################################
#Drop column by name
df18=df.drop(['ShelveLoc'],axis=1)
print(df18)

#Explictily using parameter name 'labels'
df19=df.drop(labels=["US"],axis=1)
df19

#Alternativly you can also use columns insted of labels
df20=df.drop(columns=["US"],axis=1)
df20

#Drop column by index
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
print(df.drop(df.columns[1],axis=1))

#using inplace=True
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df.drop(df.columns[[2]],axis=1,inplace=True)
df

#Drop two or more columns by level name
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df21=df.drop(["Sales","Price"],axis=1)
df21

#Drop two or more columns by index
df22=df.drop(df.columns[[0,1]],axis=1)
df22

#Drop columns from list of columns
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
lisCol=["Sales","Age"]
df23=df.drop(lisCol,axis=1)
df23
#####################################################33
#pandas Select rows by index(position/label)
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df24=df.iloc[:,0:2]
df24

df25=df.iloc[1:5,0:2]
df25

#select rows by integer index
df26=df.iloc[2]
df26

#select rows by index list
df27=df.iloc[[2,3,4]]
df27

#select row by integer index range
df28=df.iloc[1:3]
df28

#Select first row
df29=df.iloc[:1]
df29

#for first 5
df30=df.iloc[:5]
df30

#select last row
df31=df.iloc[-1:]
df31

#select alternativ rows
df32=df.iloc[::2]
df32

#select row by index label
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df33=df.loc[2]
df33
#select rows by index label
df34=df.loc[[2,3,5]]
df34

#select rows by label index
df35=df.loc[1:8]
df35

#select alternative label index
df36=df.loc[1:8:2]
df36
########################################
#select multiple columns
df37=df.loc[:,["Sales","Age","CompPrice"]]
df37


#select columns between two cloumns
df39=df.loc[:,'Sales':'Population']
df39

#select column by range
df40=df.loc[:,'Income':]
df40

#select every alternative colmn
df41=df.loc[:,::2]
df41

#Pandas.DataFrame.query() by example
df42=df.query("Sales=='4.15'")
df42
###########################################

#not equals condition
df43=df.query("zn != '25'")
df43
####################################
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df
#pandas rename column name
#rename  single column
df44=df.rename(columns={'Sales':'Total_sales'})
df44.columns

#for multiple columns
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df45=df.rename(columns={'Sales':'Total_sales','Price':'Amount','Income':'Total_Income'})
df45

#axis=1 or axis='columns'
df46=df.rename({'Sales':'Total_sales'},axis=1)
df46
df47=df.rename({'Price':'Amount'},axis='columns')
df47

row_count=len(df.index)
row_count
row_count=len(df.axes[0])
row_count

#return number of rows
row_count=df.shape[0]
row_count
#return no of columns
col_count=df.shape[1]
col_count


###########################################
#using dataframe.apply() to apply function add column

#using apply function single column
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df
def add_4(x):
    return x+4
df49=df["Sales"].apply(add_4)
df49

#apply to multiple columns
def add_10(x):
    return x+10
df50=df[['Sales','Age']].apply(add_10)
df50

#apply lambda fun to single column
df51=df["Sales"].apply(lambda x:x-2)
df51

#using DataFrame.transform()
def add_2(x):
    return x+2
df52=df['Sales'].transform(add_2)
df52

#using pandas>dataframe.map() to single column

df52=df['Sales'].map(lambda Sales: Sales/2.)
df52

####################################

#using numpy function on single column
#using dataframe.apply() and [] operator
import numpy as np
df53=df['Sales'].apply(np.square)
df53
#######################################
#using Numpy.square() method
#using numpy.square() and [] operator
df54=np.square(df['Age'])
df54

#groupby() function
#for single column
df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df55=df.groupby(['Age']).sum()
df55
##########################################3

#group by multiple columns
df56=df.groupby(['Sales','Age']).sum()
df56
######################################
#add index to the groupby data
#add row index to the group by result
df57=df.groupby(['Sales','Age']).sum().reset_index()
df57
################################

df=pd.read_csv('D:/PARESH1_python/Company_Data.csv')
df.columns

#get the list of all column names from header
columns_header=list(df.columns.values)
print("The column Header:",columns_header)

#####################################
#using list(df) to get the column headers as a list
column_headers=list(df.columns)
column_headers

#using list(df) to get the list of all column names
column_headers=list(df)
column_headers
###################################

#pandas shuffle Dataframe rows
#shuffle the DataFrame rows and return all rows

df58= df.sample(frac=1)
df58
#######################################

#create a new index starting from zero
df59=df.sample(frac=1).reset_index()
df59
#########################

#Drof shuffle index
df60=df.sample(frac=1).reset_index(drop=True)
df60
