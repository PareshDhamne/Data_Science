# -*- coding: utf-8 -*-
"""
Created on Tue May 30 23:25:31 2023

@author: Hp
"""

import pandas as pd
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
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
df['Name']

##Accessing two columns contents
df[['Name','Review']]
df
################################
################################
#select certain rows and assign it to another dataframe
df1=df[100:]
df1

#accessing certain cell from column
df['Name'][2]

#Describe DataFrame
df.describe()
######################################
######################################
#rename() – Renames pandas DataFrame columns
df.columns=['1','2','3','4','5','6','7','8','9']
df

# Rename Column Names using rename() method
df3=df.rename({'1':'A','2':'B'},axis=1) 
df3
df4=df.rename({'3':'C','4':'D'},axis='columns')
df4
df5=df.rename(columns={'1':'A','2':'B','3':'G','4':'H'})
df5
###########################################
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
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
df15=df.astype({"Name":str,"Review":int})
print(df15.dtypes)

#convert data type for all columns in a list
df.dtypes
cols=['Name','Review']
df[cols]=df[cols].astype('float')
df.dtypes

#ignores error
df16=df.astype({"Name":int},errors='ignore')
df16.dtypes

#Generates error
df17=df.astype({"Name":str},errors='raise')
df17.dtypes
###############################################
###############################################
#Drop column by name
df18=df.drop(['Bean_Type'],axis=1)
print(df18)

#Explictily using parameter name 'labels'
df19=df.drop(labels=["Bean_Type"],axis=1)
df19

#Alternativly you can also use columns insted of labels
df20=df.drop(columns=["Bean_Type"],axis=1)
df20

#Drop column by index
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
print(df.drop(df.columns[1],axis=1))

#using inplace=True
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
df.drop(df.columns[[2]],axis=1,inplace=True)
df

#Drop two or more columns by level name
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
df21=df.drop(["Company_Location","Bean_Type"],axis=1)
df21

#Drop two or more columns by index
df22=df.drop(df.columns[[0,1]],axis=1)
df22

#Drop columns from list of columns
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
lisCol=["Company_Location","Bean_Type"]
df23=df.drop(lisCol,axis=1)
df23
#####################################################
#pandas Select rows by index(position/label)
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
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
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
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
########################################
#select multiple columns
df37=df.loc[:,["Name","REF","Origin"]]
df37


#select columns between two cloumns
df39=df.loc[:,'Name':'Origin']
df39

#select column by range
df40=df.loc[:,'Rating':]
df40

#select every alternative colmn
df41=df.loc[:,::2]
df41

#Pandas.DataFrame.query() by example
df42=df.query("Rating=='4.15'")
df42
###########################################

#not equals condition
df43=df.query("REF != '25'")
df43
####################################
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
df
#pandas rename column name
#rename  single column
df44=df.rename(columns={'Name':'Nam'})
df44.columns

#for multiple columns
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
df45=df.rename(columns={'Name':'Full_NAme','COmpany_Location':'Location'})
df45

#axis=1 or axis='columns'
df46=df.rename({'Name':'Full_Name'},axis=1)
df46
df47=df.rename({'Name':'Full_NAme'},axis='columns')
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
####################################

#using numpy function on single column
#using dataframe.apply() and [] operator
import numpy as np
df53=df['Rating'].apply(np.square)
df53
#######################################
#using Numpy.square() method
#using numpy.square() and [] operator
df54=np.square(df['Rating'])
df54

#groupby() function
#for single column
df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
df55=df.groupby(['Rating']).sum()
df55
##########################################3

#group by multiple columns
df56=df.groupby(['REF','Review']).sum()
df56
######################################
#add index to the groupby data
#add row index to the group by result
df57=df.groupby(['REF','Review']).sum().reset_index()
df57
################################

df=pd.read_excel('D:/PARESH1_python/Coca_Rating_Ensemble.xlsx')
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
