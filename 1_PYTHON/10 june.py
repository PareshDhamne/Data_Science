# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 08:20:53 2023

@author: Hp
"""
'''
In python, aassignment statements (obj_b)
'''
#Assignment operation
#this will only create a new variable with the same refeence.Modifying one will affect the other.
list_a=[1,2,3,4,5]
list_b=list_a

list_a[0]= -10
print(list_a)
print(list_b)
#########################################

#shallow copy
#one level deep. Modifying on level 1 does not affect the other list.
#use copy.copy() , or object-specific copy functions/copy constructors
import copy
list_a =[1,2,3,4,5]
list_b=copy.copy(list_a)
##not affects the other list
list_b[0]=-10
print(list_a)
print(list_b)
##########################################

#But with nested objexts, modifying on level 2 or deeper does affect the other!
import copy
list_a =[[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.copy(list_a)
#affect the other!
list_a[0][0]= -10
print(list_a)
print(list_b)
#########################################

#deep copies
#full independent clones. Use copy.copy.deepcopy().
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

#not affect the other
list_a[0][0] =-10
print(list_a)
print(list_b)


