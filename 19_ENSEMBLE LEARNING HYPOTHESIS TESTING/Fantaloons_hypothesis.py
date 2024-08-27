# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:39:16 2024

@author: Paresh DHamne

Problem:
    Fantaloons Sales managers commented that % of males versus females walking into the store differ based on day of the week. 
    Analyze the data and determine whether there is evidence at 5 % significance level to support this hypothesis. 
    
Business Objective :

Maximize : To equilize the working hours of the male and female in the store

Minimize : The difference between the working hours in Female and male
workers.

Business Contraints : The data of working hours given by the company workers should
be in proper and True
"""

import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats

#########################Chi- square -test#######################3
Fantaloons=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Hypothesis/Fantaloons.csv")
Fantaloons


Fantaloons.isnull().sum()
'''
Out[8]: 
Weekdays    25
Weekend     25
dtype: int64
'''

#remove null values from datasets
Fantaloons=Fantaloons[0:400]
Fantaloons

count=(Fantaloons['Weekdays'].value_counts(),Fantaloons['Weekend'].value_counts())
count
'''
Out[12]: 
(Weekdays
 Female    287
 Male      113
 Name: count, dtype: int64,
 Weekend
 Female    233
 Male      167
 Name: count, dtype: int64)
'''

Chisquares_results= scipy.stats.chi2_contingency(count)

Chi_square=[['Test Statistic','p-value'],[Chisquares_results[0],Chisquares_results[1]]]

Chi_square
'''
Out[15]: [['Test Statistic', 'p-value'], [15.434065934065934, 8.54342267020237e-05]]
'''
'''
you use chi2_contingency when you want to test
whether two  (or more) gruops have the same distribution
'''
#H0=Null Hypothesis: there is  no significant differance between male and female at whole week
#H1=Alternative hypothesis: there is significant differance between male and female at whole week
#since p=8.54342267020237e-05<0.05 hence H0 is true 

'''
Since the p-value (8.54e-05) is much smaller than the significance level of 0.05, we reject the null hypothesis.
based on the analysis, we can conclude that there is evidence to support the hypothesis that the percentage of males versus females 
walking into the Fantaloons store differs based on the day of the week.
'''