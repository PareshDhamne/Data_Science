# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:05:03 2023

@author: Hp
"""

#store that password in file.
#sha256 is 32 bit and sha512 is 64 bit
#hexdigits
#selection of users
#election of passwords
#verification of password
#creation of hashcode for password
#store password in json file
#get username and password from user
#once the user give username and passwor check userlist and password
#prompt the user you are allowing froma ccess
#count attempt 1 2 3 etc
        
import random
import string
import json
import hashlib
#selection of user
passwords=[ ]
current_users=[ ]
new_users =[ ] 
new=input("Enter the new user:")
new_users.append(new)
print(new_users)
for new_user in new_users:
    if new_user in current_users:
        print("Person will need to enter a new username.")
    else:
        print("Saying that the username is available.. ")
current_users.append(new_users)
print(current_users)
#selection of password
passwords=[ ]
def passw(password):
    
    if len(password)<8:
        return False
    
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
def generate_password():
    while True: 
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
        if passw(password):
            print(f"the generated password: {password}, is strong!\n")
        else:
            print(f"the generated password: {password}, is weak!\n")
            
        choice=input("do you want another password? (y/n): ")
        
        if choice == "n":
            return password
       
password = generate_password()
passwords.append(password)
print(passwords) 
lst=[ ]
c=hashlib.sha512(password.encode('utf-8')).hexdigest()
lst.append(c)
print(lst)
recent_password = ""
recent_password=password
print(recent_password)
print("\nRegistration Successfull!")
print("\n\n",new_user,recent_password,lst,"\n\n")
data = {}
def login():   
    
    count = 0
    
    while True:
        user = input("enter username: ")
        if user not in current_users:
            print("user not found!, try again")
        elif count==3:
            count=0
            print("too many attempts, try after some time.")
        else:
            break
        count+=1
        
    count = 0
    attempt=False
    
    while True:
        password = input("enter password:")
        encode_password = lst
        print(password,encode_password,"\n")
        if lst passwords:
            if data[user]==encode:
                attempt=True
                break
            else:
                print("invalid password\n")
        elif count==3:
            break
        else:
            print("invalid password\n")
        count+=1
        
    if attempt:
        print("Login Successfull!")
    