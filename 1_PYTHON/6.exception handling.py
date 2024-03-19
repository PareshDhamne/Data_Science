# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:13:08 2023

@author: Hp
"""
#error occures mostly due to the absence of system rsources
#exceptional handling occur at run time and compile time

print(5/0)
#using try and except block
try:
    print(5/0)
except ZeroDivisionError:
    print("Can't divide by zero")


print("Give me two numbers, I'll divide them.")
print("Enter 'q' to quite.")
while True:
    first_number = input("\n First number:")
    if first_number == 'q':
        break
    second_number = input("\n Second number:")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
    
#handling the filenotfound error
filename = "1.txt"
with open(filename, encoding='utf-8') as f:
    contents = f.read()
    
filename = "1.txt"
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry")
    print('done')