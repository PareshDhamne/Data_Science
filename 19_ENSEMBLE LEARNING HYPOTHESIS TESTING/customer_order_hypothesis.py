# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:17:25 2024

@author: Paresh Dhamne

Problem:
    Telecall uses 4 centers around the globe to process customer order forms. 
    They audit a certain % of the customer order forms. Any error in order form renders it defective 
    and must be reworked before processing. The manager wants to check whether the defective % varies by center. 
    Please analyze the data at 5% significance level and help the manager draw appropriate inferences 

Business Objective :
    
Maximize : The analysis of the defective form and providing the best service,
on time service to the customer

Minimize : The Count of the errror forms should be minimize so the data
will be process further

Business contraints : The accuracy of the data fill by the customer and te
security of the data

"""
import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats

#########################Chi- square -test#######################3
Cust_ord=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Hypothesis/CustomerOrderform.csv")
Cust_ord


Cust_ord.isnull().sum()
'''
Out[12]: 
Phillippines    15
Indonesia       15
Malta           15
India           15
dtype: int64
'''

#remove null values from datasets
Cust_ord=Cust_ord[0:300]
Cust_ord

count=(Cust_ord['Phillippines'].value_counts(),Cust_ord['Indonesia'].value_counts(),Cust_ord['Malta'].value_counts(),Cust_ord['India'].value_counts())
count
'''
Out[18]: 
(Phillippines
 Error Free    271
 Defective      29
 Name: count, dtype: int64,
 Indonesia
 Error Free    267
 Defective      33
 Name: count, dtype: int64,
 Malta
 Error Free    269
 Defective      31
 Name: count, dtype: int64,
 India
 Error Free    280
 Defective      20
 Name: count, dtype: int64)
'''

Chisquares_results= scipy.stats.chi2_contingency(count)

Chi_square=[['Test Statistic','p-value'],[Chisquares_results[0],Chisquares_results[1]]]

Chi_square
'''
Out[25]: [['Test Statistic', 'p-value'], [3.8589606858203545, 0.2771020991233144]]
'''
'''
you use chi2_contingency when you want to test
whether two  (or more) gruops have the same distribution
'''
#H0=Null Hypothesis: the 4 group have no significant differance
#H1=Alternative hypothesis: the 4 group have significant differance
#since p=0.27710>0.05 hence H1 is true 

'''
Since the p-value (0.2771) is greater than the significance level of 0.05, we fail to reject the null hypothesis.
based on the analysis, we cannot conclude that there is a significant difference 
in the defective percentage among the four centers.
'''