# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:09:27 2024

@author: Hp

Problem: 
    A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units.
    A randomly selected sample of cutlets was collected from both units and measured? Analyze the data 
    and draw inferences at 5% significance level. 
    Please state the assumptions and tests that you carried out to check validity of the assumptions. 


Business Objective :
    
maximize : The exact prediction and measurement of the diameter of the cutlets between
            two unnits
            
Minimize : The False measures of the diameter and the wrong prediction.

Business Contraints : The accuracy of the Data Provided to us as well as the 
                    required parameters to measure the diameter
"""
import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats

#################2-sample T test for equal_variance##################
# load the dataset
cutlet=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Hypothesis/Cutlets.csv")
cutlet

#Rename the column name
cutlet.columns=cutlet.columns.str.replace(' ', '_')
cutlet.columns
#H0:There is no difference between Unit A and Unit B
#H1:There is difference between Unit A and Unit B

cutlet=cutlet[0:35]
cutlet.columns="Unit_A","Unit_B"
cutlet

#normality test
stats.shapiro(cutlet.Unit_A)  #shapiro test
#ShapiroResult(statistic=0.9649459719657898, pvalue=0.31998491287231445)

stats.shapiro(cutlet.Unit_B)
#Out[14]: ShapiroResult(statistic=0.9727305769920349, pvalue=0.5225146412849426)
#data are normal

#variance test
help(scipy.stats.levene)

#H0=both column have equal variance
#H1= both the column has not equal variance
scipy.stats.levene(cutlet.Unit_A,cutlet.Unit_B)
#Out[16]: LeveneResult(statistic=0.6650897638632386, pvalue=0.4176162212502553)
#p-value=0.417616221>0.5 so p high null fly=> Equal variance

#2 sample T test
scipy.stats.ttest_ind(cutlet.Unit_A,cutlet.Unit_B)
#Out[17]: TtestResult(statistic=0.7228688704678063, pvalue=0.4722394724599501, df=68.0)

help(scipy.stats.ttest_ind)

#Ho= equal mean
#Ha :unequal mean
#p-value =0.4722394>0.5 so p high null fly

'''
Since the p-value (0.4722) is greater than 0.05, fail to reject the null hypothesis.
Based on the analysis, we cannot conclude that there is a significant difference 
in the diameter of the cutlet between the two units.
So it is alternative hypothesis
'''


