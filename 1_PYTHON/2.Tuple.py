# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 08:19:37 2023

@author: Hp
"""

#Break loop statement
print("Only print code if all iterations completed")
num = int(input('Enter the number to check for:'))
for i in range(0,6):
    if i == num:
        break
    print(i,' ',end='')
print('Done')

print("Only print code if all iterations completed")
num = int(input('Enter the number to check for:'))
for i in range(0,6):
    if i == num:
        break
    print(i,' ',end='')
    print('Done')
    
#TUPLE

tup1 = (1,3,5,6,7)
#access elemnts of tuple
print(f'tup1[0]:\t{tup1[0]}')
print(f'tup1[1]:\t{tup1[1]}')
print(f'tup1[2]:\t{tup1[2]}')
print(f'tup1[3]:\t{tup1[3]}')
print(f'tup1[4]:\t{tup1[4]}')

tup2 = (1,'a',5,'Apple')
print(tup2)

#iterating over tuples
tup3 = ('apple','mango','banana')
for x in tup3:
    print(x)
for i in range(3):
    print(tup3[i])
    
#range for loop
for i in range(4):
    print(tup2[i])

#tuple related function
len(tup2)

#count duplicate elements
t4=('apple','mango','banana','apple')
t4.count('apple')
print(t4.index('apple'))
print(t4.index('banana'))

#checking if an element is exist or not
if 'apple' in t4:
    print('apple is there')
if 'palm' in t4:
    print('palm is there')

#nested tuples
t1 = (1,3,5,6,7)
t2 = (1,'a',5,'Apple')
t3 = ('apple','mango','banana',t1,t2)
print(t3)

##LISTS
#list are mutable
l1 = ['john','ram','laxman','rahul']
print(l1)

l1 = [1,3.5,True]
l2= ['apple','banana',35]
l1.append(l2)
l1
root = ['kaka',l1,l2,'Boss']
print(root)

#accessing elements from list
li1 = ['john','ram','laxman','rahul']
print(li1[1:])
print(li1[1:3])
print(li1[-1:-3])
print(li1[-3:-1])
li1[2]
li1[1:]
lst1 = ['john','ram','laxman','rahul']
lst1.append('Sam')
print(lst1)


lst1.insert(1,'MAhi')
print(lst1)

lst1.extend(['apple','mango'])
print(lst1)
