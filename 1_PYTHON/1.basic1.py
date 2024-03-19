# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:00:59 2023

@author: Hp
"""

print("Hello World")
x=1
print(x)
print(type(x))
x=1000000000000000000000000000000000000000000
print(x)
print(type(x))

age = input('Please enter your age:')
print(type(age))
print(age)

age = input('Please enter your age:')
print(type(age))
print(age)

age1 = input('Please enter your age1:')
print(type(age1))
print(age1)

age2 = input('Please enter your age2:')
print(type(age2))
print(age2)

age=age1+age2
print(age)

age = int(input('Please enter your age:'))
print(type(age))
print(age)

age1 = int(input('Please enter your age1:'))
print(type(age1))
print(age1)

age2 = int(input('Please enter your age2:'))
print(type(age2))
print(age2)

age=age1+age2
print(age)

int_value = 100
#string_value ='1.5'
float_value = float(int_value)
print('int value as a float:',float_value)
print(type(float_value))

float_value = 100.0
int_value = int(float_value)
print(int_value)
print(type(int_value))

#complex number
c1=1
c2=2j
print('c1',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#boolean values

all_ok = True
print(all_ok)

all_ok = False
print(all_ok)
print(type(all_ok))

#You can also convert strings into bool form
status = bool(input('Ok it is conform:'))
print(status)
print(type(status))

#arithmetic operators

home = 10
away = 15
print(home+away)
print(type(home+away)) 


print(10*4)
print(type(10*4))
goals_for = 10

print(100 / 20)
print(type(100 / 20))

#floor division
print(100 // 20)
print(type(100 // 20))

#modulus division
print('Modulus division 100 %13 :',100 % 13)
print('Modulus division 5 % 3:',5 %3)

#power operator
a = 5
b = 3
print(a**b)
print(b**a)
#assignment operator
x = 0
x += 1
print(x)

#none value
winner = None
print(winner is None)

winner = None
print('Winner',winner)
print(type(winner))

#identation

num = int(input('Enter a number:'))
if num > 0:
    print(num)

num = int(input('Enter a number:'))

#elese in an if statement
num=int(input('Enter yet another number:'))
if num < 0:
    print('Its negative')
else:
    print('Positive')
    
#The Use of elif
savings = float(input('Enter how much you have in saving:'))
if savings == 0:
    print("sorry no saving")
elif savings < 500:
    print("Well done")
elif savings <1000:
    print("Welcome sir")
else:
    print('Thank You')

#while loop
count = 1
print('Starting')
while (count <= 10):
    print(count)
    count+=1

#for loop
print('Values in a range')
for i in range(2,10):
    print(i)










#for anaymous 
for _ in range(0,10):
    print('.')
    






































































for i in range(2,10):
    print(i)
    print('doNE')

print('Only print code if all iterations completed')
num=int(input('Enter a number:'))
for i in range(0, 16):
    if i == num:
        break
    print(num)
    
for _ in range(0,10):
    print('.',end='')
    print()


