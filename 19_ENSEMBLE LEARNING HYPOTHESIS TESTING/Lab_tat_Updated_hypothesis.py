# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:59:54 2024

@author: Paresh Dhamne

Problem:
    A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories 
    on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. 
    TAT is defined as sample collected to report dispatch. 
    Analyze the data and determine whether there is any difference in average TAT among the different laboratories 
    at 5% significance level. 

"""

import pandas as pd
import numpy as np
import scipy
from scipy import stats 


# from statmodels.stats import weightstats sa stests
import statsmodels.stats.weightstats

#########one Way- Anova###########
# load the dataset
lab_tat=pd.read_csv("D:/12-SUPERVISED ALGORTIHM/Hypothesis/lab_tat_updated.csv")
lab_tat

#H0= All the 4 labs have equal mean turn around time (TAT)
#H1= All the 4 labs have not equal mean turn around time (TAT)

#normality test
stats.shapiro(lab_tat.Laboratory_1)    #shapiro test
#Out[8]: ShapiroResult(statistic=0.9886695146560669, pvalue=0.4232051372528076)
#pvalue=0.42>0.005 Laboratory_1 is normal

stats.shapiro(lab_tat.Laboratory_2)    #shapiro test
#Out[9]: ShapiroResult(statistic=0.9936320185661316, pvalue=0.8637352585792542)
#pvalue= 0.86373 > 0.05 Laboratory_2 is normal

stats.shapiro(lab_tat.Laboratory_3)    #shapiro test
#Out[10]: ShapiroResult(statistic=0.9796065092086792, pvalue=0.06546738743782043)
#pvalue=pvalue=0.065467>0.05 Laboratory_3 is normal

stats.shapiro(lab_tat.Laboratory_4)    #shapiro test
#Out[11]: ShapiroResult(statistic=0.9913760423660278, pvalue=0.6619619131088257)
#pvalue=pvalue=0.66196>0.05 Laboratory_4 is normal

#variance test
help(scipy.stats.levene)
#all 4 labs are being checked for variance
scipy.stats.levene(lab_tat.Laboratory_1,lab_tat.Laboratory_2,lab_tat.Laboratory_3,lab_tat.Laboratory_4)
#Out[13]: LeveneResult(statistic=1.025294593220823, pvalue=0.38107781677304564)
# the levene test tests the null hypothesis
# that all input samples are from populations with equal variance
#pvalue=0.38107>0.05, p is hgh null fly
#H0= All input samples are form population with equla varaince

#one- way Anova
F, p=stats.f_oneway(lab_tat.Laboratory_1,lab_tat.Laboratory_2,lab_tat.Laboratory_3,lab_tat.Laboratory_4)

#p value
p  
#Out[15]: 2.143740909435053e-58
# p high null flky
# all the 4 labs have equal mean turn around time (TAT)

'''
Since the p-value (2.14e-58) is significantly smaller than 0.05, we reject the null hypothesis.
based on the analysis, you can conclude that there is a significant difference in the average Turn Around Time (TAT) 
among the different laboratories.
'''





 

