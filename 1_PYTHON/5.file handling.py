# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:37:08 2023

@author: Hp
"""
#file handling
with open('1.txt') as file_object:
    contents = file_object.read()
print(contents)
    
#observe the extra line at the end of output
#to avoid the rstrip() method is used
with open('1.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

#rstrip() removes or strips any whitespaces

file_path = "D:/PARESH1_python/1.txt"
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())

#reading line by line
filename = "1.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line)
        
filename = "1.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#readline method
#the readline method takes each line from the 
filename = "1.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

#working with a file contents
#you  can do whatever you want with data
filename = "1.txt"
with open(filename) as file_object: 
    lines = file_object.readlines()
    pi_string=' '
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))
        
#writing to file
filename = '1.txt'
with open(filename,'w') as file_object:
    file_object.write("Hello! How are you?")
with open('1.txt') as file_object:
    contents = file_object.read()
print(contents)

    
#writing multiple lines

filename = '1.txt'
with open(filename,'w') as file_object:
    file_object.write("Hello! How are you?")
    file_object.write("- I am fine. and You?")
with open('1.txt') as file_object:
    contents = file_object.read()
print(contents)

#newline
filename = '1.txt'
with open(filename,'w') as file_object:
    file_object.write("Hello! How are you?")
    file_object.write("\n- I am fine. and You?")
with open('1.txt') as file_object:
    contents = file_object.read()
print(contents)

#appending to file
filename = '1.txt'
with open(filename,'a') as file_object:
    file_object.write("\n I am also fine.")
    file_object.write("\n- ok bye")
with open('1.txt') as file_object:
    contents = file_object.read()
print(contents)
    
      


    
