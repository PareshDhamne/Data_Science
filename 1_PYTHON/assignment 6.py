# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:44:26 2023

@author: Hp
"""
#password picker
import string
#pick the adjectives
adjectives = ['sleepy','slow','smelly','wet','fat','red','orange',
              'yellow','green','blue','purple','fluffy',
              'white','brave']

#pick the nouns
nouns = ['apple','dinosaur','ball','toaster','goat','gragon',
         'hammer','duck','panda']

#pick the word
import random
adjective = random.choice(adjectives)
noun = random.choice(nouns)

#select a number
number = random.randrange(0, 100)
#select a special character

special_char = random.choice(string.punctuation)

#create the new secure code
password = adjective + noun + str(number)+ special_char
#%s is for string format
print('Your new password is:%s' %password)

#another one?
#for another password used whule loop
print('Welocme to password Picker!')
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number)+ special_char
    print('Your new password is:%s' %password)
    response = input("Would you like another password (y/n)?:")
    if response == 'n':
        break









#input from user append list
import random
import string
n = [ ]
adj = input('Enter the adjective:')
n.append(adj)
print(n)
adjective = random.choice(n)

a = [ ]
noun = input("Enter the noun: ")
a.append(noun)
print(a)
noun = random.choice(a)
adj = random.choice(n)
number = random.randrange(0, 100)
special_char = random.choice(string.punctuation)  
password = noun + adj + str(number) + special_char
print('Your new password is:%s' %password)


def passw(password):
    lower = False
    upper = False
    number = False
    special = False
    
    for a in password:
        if a>='a' and a<='z':
            lower='True'
        elif a>='A' and a<='Z':
            upper='True'
        elif a>='0' and a<='9':
            number = True
        elif a in string.punctuation:
            special=True
    if lower and upper and number and special:
        return True
    return False
x  = input("Enter the Password:")
print(passw(x))
        
