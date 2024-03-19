# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:42:59 2023

@author: Hp
"""

#ASSIGNMENT
import pandas as pd
df=pd.read_csv('D:/PARESH1_python/boston_data.csv')
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
df['indus']

##Accessing two columns contents
df1=df[['crim','age']]
df1
################################
#select certain rows and assign it to another dataframe
df2=df[300:]
df2

#accessing certain cell from column
df['crim'][2]

#Describe DataFrame
df.describe()
######################################
#rename() – Renames pandas DataFrame columns
df.columns=['1','2','3','4','5','6','7','8','9','10','11','12',
            '12','13']
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

df9=df.drop(df.index[400:])
df9

# Delete Rows by Index Range
df10=df.drop(df.index[14:])
df10

#for default
df11=df.drop(0)
df11
#######################################
#Select Rows by Index
df12=df[10:300]
df12

#converting all types to best possible types
df13=df.convert_dtypes()
print(df13.dtypes)

#change all columns to same type
df14=df.astype(str)
print(df14.dtypes)

#change type for one or more multiple columns
df=pd.read_csv('D:/PARESH1_python/boston_data.csv')
df15=df.astype({"crim":int,"indus":int})
print(df15.dtypes)

#convert data type for all columns in a list
df.dtypes
cols=['chas','nox']
df[cols]=df[cols].astype('float')
df.dtypes

#ignores error
df16=df.astype({"nox":int},errors='ignore')
df16.dtypes

#Generates error
df17=df.astype({"chas":int},errors='raise')
df17.dtypes
###############################################33
#Drop column by name
df18=df.drop(['chas'],axis=1)
print(df18)

#Explictily using parameter name 'labels'
df19=df.drop(labels=["zn"],axis=1)
df19

#Alternativly you can also use columns insted of labels
df20=df.drop(columns=["chas"],axis=1)
df20

#Drop column by index
df=pd.read_csv('D:/PARESH1_python/boston_data.csv')
print(df.drop(df.columns[1],axis=1))

#using inplace=True
df=pd.read_csv('D:/PARESH1_python/boston_data.csv')
df.drop(df.columns[[2]],axis=1,inplace=True)
df

#Drop two or more columns by level name
df=pd.read_csv('D:/PARESH1_python/boston_data.csv')
df21=df.drop(["chas","age"],axis=1)
df21

#Drop two or more columns by index
df22=df.drop(df.columns[[0,1]],axis=1)
df22

#Drop columns from list of columns
df=pd.read_csv('D:/PARESH1_python/boston_data.csv')
lisCol=["chas","age"]
df23=df.drop(lisCol,axis=1)
df23
#####################################################33
#pandas Select rows by index(position/label)
df=pd.read_csv('D:/PARESH1_python/boston_data.csv')
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
df=pd.read_csv('D:/PARESH1_python/boston_data.csv')
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

#select multiple columns
df37=df.loc[:,["crim","age","zn"]]
df37

#select random columns
df38=df.loc[:,["crim","age","zn"]]
df38

#select columns between two cloumns
df39=df.loc[:,'crim':'rad']
df39

#select column by range
df40=df.loc[:,'rad':]
df40

#select every alternative colmn
df41=df.loc[:,::2]
df41

#Pandas.DataFrame.query() by example
df42=df.query("zn=='25'")
df42
###########################################

#not equals condition
df43=df.query("zn != '25'")
df43

#########################################


#05-05-2023

#pandas add colmn to dataframe

import pandas as pd
import numpy as np
technologies=({
    'courses':['spark','pyspark','Hadoop','python','pandas'],
    'Fee':[20000,10000,50000,1000,900],
    'Duration':['30days','40days','25days','10days','80days'],
    'Discount':[1000,2300,1500,1000,200]
    })
df=pd.DataFrame(technologies)
df

#pands add colmn to dataframe
#add new colmn to dataframe
tutors=["Ram","Shyam","Harry","piter","Nilesh"]
df2=df.assign(TutorsAssigned=tutors)
df2

#add multiple columns to the dataframe
MNCCompanies=['tata','h&c','infosys','amazon','flipkart']
df3=df.assign(MNCComp=MNCCompanies,TutorsAssigned=tutors)
df3
###############################

#derive new column from existing column
df=pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x:x.Fee * x.Discount/100)
df2

#append column to existing pandas dataframe
#add new column to the existing Dataframe
df=pd.DataFrame(technologies)
df["MNCCompanies"]=MNCCompanies
df
#####################################
#Add new column at the specific position
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
df
################################

#pandas rename column with exzmples
import pandas as pd
import numpy as np
technologies=({
    'courses':['spark','pyspark','Hadoop','python','pandas'],
    'Fee':[20000,10000,50000,1000,900],
    'Duration':['30days','40days','25days','10days','80days']
    })
df=pd.DataFrame(technologies)
df.columns
print(df.columns)

#pandas rename column name
#rename  single column
df2=df.rename(columns={'courses':'Courses_List'})
df2.columns

#for multiple columns
df=pd.DataFrame(technologies)
df2=df.rename(columns={'courses':'Courses_List','Fee':'Amount','Duration':'Time'})
df2

#axis=1 or axis='columns'
df1=df.rename({'courses':'Courses_List'},axis=1)
df1
df2=df.rename({'courses':'Courses_List'},axis='columns')
df2

###############################################
#quick examples of get the number of rows in dataframe
import pandas as pd
import numpy as np
technologies=({
    'courses':['spark','pyspark','Hadoop','python','pandas'],
    'Fee':[20000,10000,50000,1000,900],
    'Duration':['30days','40days','25days','10days','80days']
    })
df=pd.DataFrame(technologies)
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