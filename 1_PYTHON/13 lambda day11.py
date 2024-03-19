# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:23:07 2023

@author: Hp
"""
#lambda function is used for code optimization

def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))

add=lambda a,b,c:a+b+c
add(4,5,6)
#################################

def mul(a,b,c):
    multi=a*b*c
    return multi
print(mul(4,5,6))

mul=lambda a,b,c:a*b*c
mul(4,5,6)
####################################
#*args is a arbitary parameter used to insert many values
val=lambda *args:sum(args)
val(5,6,7,8,43,2)
#############################################
def myfun(*args):
    for i in args:
        print(i)
myfun("Hello","Python","how","are","you")
myfun("This","is","python")

myfun = lambda *args:[print(i) for i in args]

#######################################################
def person(name,*data):
    print(name)
    print(data)
person("navin",28,"Munbai",9875)
person=lambda name,*data:print(name,data)
###########################
#**args is keyword argument used to store keys and values
def person(name,**data):
    print(name)
    print(data)
person(name="navin",age=28,place="mumbai")
person=lambda name,**data:(name,(data))
####################################

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name="navin",age=28,place="mumbai")
###################################

val=lambda **data:sum(data.values())
val(a=2,b=6,c=7,d=20)
###################################

person=lambda **data:[(i,j) for i,j in data.items()]
person(name="navin",age=28,place="mumbai")

########################################

lst1=[3,4,5,6,78]
sqr= lambda lst1:[i**2 for i in lst1]
print(sqr(lst1))
######################################s
