# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:47:48 2023

@author: Hp
"""

#write a program to find out is duplicate elements in a list

#for adjaecent elements
l1 = [1,2,3,5,6,5,5,7]
def duplicate(l1):
    for i in range(len(l1)-1):
        if(l1[i]==l1[i+1]):
            print('There is duplicate element')
            return True
    return False
print(duplicate(l1))

#for all elements
l2 = [1,2,3,5,6,7]
def duplicate(l2):
    for i in range(len(l2)):
        for j in range(len(l2)):
            if i==j:
                continue
            if(l2[i]==l2[j]):
                return True
        return False
print(duplicate(l2))


#2)Mario pyramid or dimond
for i in range(5):
    for j in range(5):
        print('#',end=' ')
    print( )
        

for i in range(5):
    for j in range(5-i):
        print('#',end=' ')
    print( )
    
for i in range(5):
    for j in range(i+1):
        print('#',end=' ')
    print( )
    
for i in range(5):
    for j in range(5-i):
        print('#',end=' ')
    print( )
for i in range(5):
    for j in range(i+1):
        print('#',end=' ')
    print( )
    
for i in range(5):
    for j in range():
        print('#', end=" ")
    print( )
    
for i in range(5):
    for j in range(i+1):
        print('#',end=' ')
    print( )
for i in range(5):
    for j in range(5-i):
        print('#',end=' ')
    print( )
    
for i in range(5):
    print(" " *(5-i),"#" * (2*i+1))
for i in range(5-2,-1,-1):
    print(" " *(5-i),"#" * (2*i+1))
    
for i in range(5):
    for j in range(i+1):
        print(' '*(5-i)'#' * (2*i+1))
    print( )
 
    

  









  
 
#1) Check whether the given number is palindrom or not.
x = input("Enter the number:")
if(x==x[::-1]):
    print("Number is paindrom")
else:
    print("Number is not palindrom")
    



#2)find min and max from given list
l1 = [1,5,3,6,8,4]
def maximum(l1):
    max = 0
    for i in l1:
        if i > max:
            max = i
    return max
def minimum(l1):
    min = 20
    for i in l1:
        if i < min:
            min = i
    return min
print(maximum(l1))
print(minimum(l1))

    
