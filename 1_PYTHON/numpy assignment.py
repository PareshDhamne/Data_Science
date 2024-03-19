# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:36:12 2023

@author: Hp
"""

import numpy as np
print(np.__version__)
print(np.show_config())

#write a nupy program to get help with he add function
print(np.info(np.add))
print(np.dot())

#Write a nupy program to test whether
x=np.array([1,2,3,4])
print("Original Array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
x=np.array([0,1,2,3])
print("Orignal array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

x=np.array([1,0,0,0])
print("Orignal array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.any(x))

x=np.array([0,0,0,0])
print("Orignal array:")
print(x)
print("Test if none of the elements of the said array is non-zero:")
print(np.any(x))

#for finite or not
a=np.array([1,0,np.nan,np.inf])
print(a)
print("Test if none of the elements of the said array is finite:")
print(np.isfinite(a))

#test element for complex number
a= np.array([1+1j,1+0j,4.5,3,2,2j])
print("orignal array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))

#############################
a=[[1,2,3],[2,3,4]]
print("Orignal array")
b=np.array(a)
b
b.ndim
b.shape
b.size
b[1,2]
b[1,1]
b[1,0]
#access thee elements of first row and 2nd column
b[0][0:2]
#############################
b[0:2,2]


#Basic operations
#Create numpy array x
x=np.array([[1,0],[0,1]])
x

y=np.array([[2,1],[1,2]])
y

#add x and y
z=x+y
z

#multiply y with x
z=y*x
z

#multiply x with y
z=x*y
z

#use for dot product
z=np.dot(x,y)
z

#calculate the sine of z
np.sin(z)

#calculate transpose of matrix
c=np.array([[1,1],[2,2],[3,3]])
c
#get teanspose of c
c.T
################################
#write a numpy progeam for multiplication of 2 matries
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print(p)
print(q)
result=np.dot(p,q)
print(result)

p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print(p)
print(q)
result=np.outer(p,q)
print(result)

#A dot product of two vectors is also called the scalar product. It is the product of the magnitude of the two vectors and the cosine of the angle that they form with each other.
#A cross product of two vectors is also called the vector product. It is the product of the magnitude of the two vectors and the sine of the angle that they form with each other.
#The difference between the dot product and the cross product of two vectors is that the result of the dot product is a scalar quantity, whereas the result of the cross product is a vector quantity.
#write a numpy program to compute the croos product of  2 vectors
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
result1=np.cross(p,q)
result2=np.cross(q,p)
print(result1)
print(result2)
######################################
#Write a numpy to compute the determinant of given square matrix
from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print(a)
print(np.linalg.det(a))
#write a numpy prgram to compute the eigenvalues and eigenvectors
#############################################
import numpy as np
m=np.mat("3 -2;1 0")
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eigne vector",w)
print("Eigen Value:",v)
#############################################
#write a numpy program to compute the inverse of a given matrix
m=np.array([[1,2],[3,4]])
print(m)
result= np.linalg.inv(m)
print(result)
##########################################
#write a numpy program to genetate five random numbers
import numpy as np
x=np.random.normal(size=5)
print(x)
##############################
#to generate six random integer
x=np.random.randint(low=10,high=30,size=6)
print(x)
########################
#to create 3x3x3 array withrandom values
x=np.random.random((3,3,3))
print(x)
##########################
#create 5x5 array wtih random values and find min and max
x=np.random.random((5,5))
print(x)
xmin,xmax=x.min(),x.max()
print(xmin,xmax)
##################################

'''
2 june 2023
'''
#Write a numpy program to get a min and max value for given array along with 2nd axis
import numpy as np
x = np.arange(4).reshape((2,2))
print(x)
#along with 2nd axis
print(np.amax(x,1))
print(np.amin(x,1))
##################################################
#write python program to draw a line with suitable label
import matplotlib.pyplot as plt
x=range(1,500)
y=[value * 3 for value in x]
print("Values of X:")
print(range(1,50))
print("Values of y(thrice of X):")
print(y)
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("line  graph")
###############################################
#write python program to draw a line using given axis values
x=[1,2,3]
y=[2,4,1]
#plot lines and/or markers to the axis
plt.plot(x,y)
#set the x axis label of the current axis
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.title("Graph")
plt.show()
#########################################
#write python program to draw line charts of the finaancial data of 
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("D:/PARESH1_python/fdata.csv")
df.plot()
plt.show()
##########################################################################

att = pd.read_csv('attendence.csv')
att


df2 = att.drop('year',axis=1)
df2 = df2.drop('month',axis=1)
df2 = df2.drop('weekday',axis=1)
df2 = df2.drop('datum',axis=1)
df2.columns

df2 = df2[:-1]

df2.plot()

##########################################################################
#write a python program for two or more lines with legends 
x1=[10,20,30]
y1=[20,30,40]

x2=[10,20,30]
y2=[10,40,30]
#set labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more lines with different widths ')
#display the figure
plt.plot(x1,y1, color='blue', linewidth=3, label='line1-width-3')
plt.plot(x2,y2, color='red',linewidth=3, label='line1-width-3')
plt.legend()
plt.show()
#####################################################

#write pytho program to plot two or more lines with diff styles
x1=[10,20,30]
y1=[20,30,40]

x2=[10,20,30]
y2=[10,40,30]
#set labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more lines with different widths ')
#display the figure
plt.plot(x1,y1, color='blue', linewidth=3, label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red',linewidth=3, label='line2-dash',linestyle='dashed')
plt.legend()
plt.show()
############################################

#write a python program to plot two or more lines and set the line markers
x=[1,4,5,6,7]
y=[2,6,3,6,3]

#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)

#set the y-limit of the curret axist
plt.ylim(1,10)

#x limit
plt.xlim(1,8)

#add labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#add title
plt.title('Display marker')
plt.show()
#########################################

#write a python program to plot several lines 
import numpy as np
import matplotlib.pyplot as plt

#sampled time at 200ms intervals
t=np.arange(0.,5.,0.2)

#green dashes, blue squares and red triangles
plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')
plt.show()
##########################################

#write a python program to display a bar chart of the popularity of programming languahge
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,.7]
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
x_pos=[i for i, _ in enumerate(x)]  #Here _ is variable and enumerate is representing languages and popularity
plt.bar(x_pos,popularity,color='blue')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("Popualarity of programming language")
plt.xticks(x_pos,x)
plt.show()
################################################
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,.7]
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
x_pos=[i for i, _ in enumerate(x)]  #Here _ is variable and enumerate is representing languages and popularity
plt.barh(x_pos,popularity,color='green')
#plt.barh is used to draw horizontal bar graph
plt.xlabel('Popularity')
plt.ylabel('Languages')
plt.title("Popualarity of programming language")
plt.yticks(x_pos,x)
plt.show()
########################################

#write python program to create bar plot of scores by group and gender. Use multiple X
import numpy as np
import matplotlib.pyplot as plt

#data to plot
n_groups=5
men_means=(22,30,33,30,26)
women_means=(25,32,30,35,29)

#create plot
fig,ax=plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

reacts1 = plt.bar(index, men_means, 
                  bar_width, 
                  alpha=opacity,
                  color='g',
                  label='Men')
reacts1 = plt.bar(index+bar_width, women_means, 
                  bar_width, 
                  alpha=opacity,
                  color='r',
                  label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index+bar_width,('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()
