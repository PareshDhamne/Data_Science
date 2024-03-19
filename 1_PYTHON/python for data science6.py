# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:30:23 2023

@author: Hp
"""

#in the input array

#to perform mod function
#on numPy array

import numpy as np
arr1=np.array([7,20,10])
arr2=np.array([3,5,2])
arr1
arr1.dtype

#Arrays in numPy

#create a multi dimensional array
#create multi dimensional array

arr=np.array([[10,20,30],[40,50,60]])
print(arr)

#represent the minimum dimension
#use ndmin param to specify how many minimum
#dimensions you wanted to create an arry with
#,minimum dimension
arr=np.array([10,20,30,40],ndmin=2)
print((arr))

arr1=np.array([10,20,30,40],ndmin=3)
arr1


#change the data type
#dtype parameter
arr=np.array([10,20,30],dtype=complex)
arr

#get the dimension of array
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)

#Finding the size of each item in the array
arr=np.array([10,20,30])
print("Each item contain in bytes:",arr.itemsize)
#################################################

#get the data type of each array item
#finding the data type of each array item

arr=np.array([10,20,30])
print("Each item is of the type",arr.dtype)

#Get the shape and size of array

arr=np.array([[10,20,30,40],[60,70,80,90]])
print("Array size:",arr.size)
print("Shape:",arr.shape)

#creating array from list with type float
arr=np.array([[10,20,40],[30,40,50]],dtype='float')
print("Array create by using list:\n",arr)

#create a sequece of integer using arange()
#create a sequence of integer
#from 0 to 20 with steps of 3

arr=np.arange(0,20,3)
print("A sequencetial array with steps of 3:\n",arr)
#############################################
#############################################

#array indexig  in numpy

#access single element using inex
arr=np.arange(11)
arr

print(arr[2])

arr[-2]
##########################################

#Multi-Dimensional array indexing
#access multi-dimensional array element
#using array indexing
arr=np.array([[10,20,30,40,50],[20,30,50,10,30]])
arr

print(arr.shape)

print(arr[1,1])

print(arr[0,4])

print(arr[1,-1])

################################################

#Access array elements using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
x

x=arr[-2:3:-1]
x

x=arr[-2:10]
x

#indexing in numpy
arr=np.array([[10,20,10,40],
              [40,50,70,90],
              [60,10,70,80],
              [30,90,40,30]])
arr

#slicing array

#for multi-dimensional numpy arrays,you can access

#multi_arr[1,2] - to access the value at row1 and column2
#multi_arr[1,:]-To get value at row 1 and all columns
#multi_arr[:,1]-To get value at column 1 and all rows

x=arr[:4,::2]
x

#integer array indexing
arr = np.arange(35).reshape(5,7)
arr

#boolean array indexing
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)

rows=np.array([False,True,True])#not 0th row only first and sec
wanted_rows=arr[rows,:] #in selected rows all rows and columns
wanted_rows

#Convert Numpy Array to the list
#we can convert the numpy array to the list

#convert one dimensional array to list

#Create array
array=np.array([10,20,30,40])
print("Array:",array)
print(type(array))

#convert list
list=array.tolist()
print("list:",list)
print(type(list))

#convert Multi Dimensional Arrray to list
arr=np.array([[10,20,10,40],
              [40,50,70,90],
              [60,10,70,80]])
print("array:",arr)

#convert list
lst=arr.tolist()
print("list:",lst)

#Convert python list to an numPyarray       
lst=[20,30,60,80]

array=np.array(lst)
array        

#USe array()
lst=[20,30,60,80]
array=np.asarray(lst)
print("Array:",array)
print(type(array))

#Numpy array properties

#ndarray.shape
#ndarray.ndim
#ndarray.itemsize
#ndarray.size
#ndarray.dtype

#ndarray.shape
array=np.array([[10,20,30],[40,50,60]])
array.shape

#resize the array
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)

#reshape usage
array=np.array([[10,20,30],[40,50,60]])
new_array=array.reshape(3,2)
new_array

#ndarray.ndim
array=np.array([[1,2,3,4],[7,8,6,7],[9,20,22,12]])
array.ndim

#Apply arithmentic operation on numpy array
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,3,2,4])

#Add()
add_arr=np.add(arr1,arr2)
print(f"Addition of two arrays:\n{add_arr}")

#subtract()
sub_arr=np.subtract(arr1,arr2)
print(f"Subtraction of two arrays:\n{sub_arr}")

#multiply()
mul_arr=np.multiply(arr1,arr2)
print(f"Multiplicationn of two arrays:\n{mul_arr}")

#divide
div_arr=np.divide(arr1,arr2)
print(f"Division of two arrays:\n{div_arr}")

#numpy reciprocal()

#this function retruns the reciprocsl of argument

#to perform Reciprocal operations
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print('After applying reciprocla function',rep_arr1)

#This numpy power() function treats elements in


#to perform power operations
import numpy as np
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f'After power function to array:\n{pow_arr1}')


arr2=np.array([3,2,1])
print("My second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"After applying power function to array:\n{pow_arr2}")


#to perform mod function
#on numpy array


import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
arr1.dtype


#create an empty array
from numpy import empty 
a=empty([3,3])
a

#create zeros array
from numpy import zeros
a=zeros([3,5])
a

#create one array
from numpy import ones
a=ones([3,5])
a

#create array with vstack
from numpy import array
from numpy import vstack
#create first array
a1=array([1,2,3])
a1
#create second array
a2=array([4,5,6])
a2

#vertical stack
a3=vstack((a1,a2))
a3
a3.shape

#create array with hstack
from numpy import array
from numpy import vstack
#create first array
a1=array([1,2,3])
a1
#create second array
a2=array([4,5,6])
a2
#create hstack
a3 = hstack((a1,a2))
a3
a3.shape

#create two dimesional array





#index a one_dimensional array
from numpy import array
#define array
data=array([11,22,33,44,55])
#index data
print(data[0])
print(data[4])

################################
#index array out of bound
from numpy import array
#define array
data=array([11,22,33,44,55])
#index data
data[5]

#negative array indexing
from numpy import array
#define array
data=array([11,22,33,44,55])
data[-1]
data[-2]

#index row of 2 d array
from numpy import array
#define array
data=array([
    [11,22],
    [33,44],
    [55,66]])
#index data
print(data[0,])

#0 th row all the column
#################################

#split input and output data
from numpy import array
#define array
data=array([
       [11,22,33],
       [44,55,66],
       [77,88,99]])

#seprate data
x, y =data[:,:-1],data[:,-1]

#data[:,:-1]-all rows and all columns
#ecxept all rows and last column
#data[:,-1] - taking all row(:)
#but keeping the last column (-1)
x
y

##################################
#brodcast scalar to one-dimensional array
from numpy import array#define array
a=array([1,2,3])
a
#define scalar
b=2
b
#brodcast
c=a+b
c
##############################
#vector addition
from numpy import array
a=array([1,2,3])
a
b=array([1,2,3])
b 
c=a+b
c

#vector subtraction
from numpy import array
a=array([2,3,4])
a
b=array([1,2,3])
b 
c=a-b
c

################################
#vector L1 norm
'''
l1 nom is sum of magnitude of the vector in aspace
||x||1=|3|+|4|=7

l2 norm is the shortest distance to go from one point to another

'''
from numpy import array
from numpy.linalg import norm
#define vector
a=array([1,2,3])
a
#calculate norm
l1=norm(a,1)
l1
#######################
#vector l2 norm
from numpy import array
from numpy.linalg import norm
#define vector
a=array([1,2,3])
a
#calculate norm
l2=norm(a)
l2
########################
#triangular matrices
from numpy import array
from numpy import tril
from numpy import triu
#define square matrix
M=array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
M
#lower triangular matrix
lower=tril(M)
lower

#upper triangular matrix
upper=triu(M)
upper
#########################

#diagonal matrix
from numpy import array
from numpy import diag
#define square matrix
M=array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
M
d=diag(M)
#create diagonal matrix
D=diag(d)
D
##################################
#identity matrix
from numpy import identity
I=identity(3)
print(I)
##########################

#orthogonal matrix
from numpy import array
from numpy.linalg import inv
#define orthogonal matrix
Q=array([
    [1,0],
    [0,-1]])
Q

#inverse equivalence
v=inv(Q)
print(Q.T)
print(v)

#identity equivalence
I=Q.dot(Q.T)
I
