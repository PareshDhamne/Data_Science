# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:12:50 2023

@author: Hp
"""

import pandas as pd
technologies={
    'courses':["spark","pyspark","Python","Hadoop"],
    'Fee':[20000,25000,26000,50000],
    'Duration':['30days','40days','50days','40days'],
    }
index_labels = ['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies, index = index_labels)

technologies2={
    'courses':["spark","Java","Python","Go"],
    'Discount':[2000,1000,1200,2000]
    }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2, index = index_labels2)

#pandas join, by default it will join the table left join
df3=df1.join(df2,lsuffix='_left',rsuffix='_right')
df3

#####################################
#pandas inner join Dataframes
df4=df1.join(df2,lsuffix='_left',rsuffix='_right',how='inner')
df4
###############################

#pandas left join dataframes
df5=df1.join(df2,lsuffix='_left',rsuffix='_right',how='left')
df5
################################################
#pandas RIGHT join dataframes
df6=df1.join(df2,lsuffix='_left',rsuffix='_right',how='right')
df6

#########################################
#pandas join on columns
df7=df1.set_index('courses').join(df2.set_index('courses'), how='inner')
df7

df8=df1.set_index('courses').join(df2.set_index('courses'), how='left')
df8

df8=df1.set_index('courses').join(df2.set_index('courses'), how='right')
df8

#pandas Merge dataframes
import pandas as pd
technologies={
    'courses':["spark","pyspark","Python","Hadoop"],
    'Fee':[20000,25000,26000,50000],
    'Duration':['30days','40days','50days','40days'],
    }
index_labels = ['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies, index = index_labels)

technologies2={
    'courses':["spark","Java","Python","Go"],
    'Discount':[2000,1000,1200,2000]
    }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2, index = index_labels2)

#using pandas.merge()
df3=pd.merge(df1,df2)
df3

#using dataframe0.merge()
df3=df1.merge(df2)
df3

df4=df1.merge(df2, how='left')
df4
##############################################################

#use pandas.concat() to concat Two DataFrames
import pandas as pd
df=pd.DataFrame({'courses':["Spark","Pyspark","Python","pandas"],
                 'Fee':[20000,10000,5000,2000]})

df1=pd.DataFrame({'courses':["pandas","Hadoop","Hyperion","Java"],
                 'Fee':[25000,12000,51000,22000]})



#using pandas.concat two dataframes
data=[df,df1]
df2=pd.concat(data)
df2

import pandas as pd
df=pd.DataFrame({'courses':["Spark","Pyspark","Python","pandas"],
                 'Fee':['20000','10000','5000','2000']})
df1=pd.DataFrame({'courses':["Unix","Hadoop","Hyperion","Java"],
                 'Fee':['25000','12000','51000','22000']})
df2=pd.DataFrame({'Duration':['30days','40days','35days','60days','55days'],
                  'Discount':[1000,2000,3000,1200,500]
                  })
#appending multiple Dataframe
df3=pd.concat([df,df1,df2])
df3

#write DataFrame to CSV file with Default params
df3.to_csv("D:/PARESH1_python/courses.csv")
#read csv

#import pandas
import pandas as pd

#read CSV file into DataFrame
df1=pd.read_csv('courses.csv')
df1

#Write DataFrame to Excel File
df.to_excel("D:/PARESH1_python/Courses1.xlsx")
######################################
import pandas as pd
#read excel file
df2=pd.read_excel("D:/PARESH1_python/Courses1.xlsx")
df2

#######################################

#series is used model one dimensional data
#similar to list in python but not list
#series object also have a few more bits
#
import pandas as pd
songs2=pd.Series([145,142,38,13],name='counts')
songs2
songs2.index
