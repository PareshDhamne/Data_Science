# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 00:28:00 2023

@author: Hp
"""

import random
import hashlib
import string

users=[]
passwords=[]
data = {}

recent_password = ""

adjectives = input("enter adjectives: ").split()
nouns = input("enter nouns: ").split()

#checking a valid password
def check(password):
    
    if len(password) < 8:
        return False
    
    lower=False
    upper=False
    number=False
    special=False
    
    for ch in password:
        
        if ch>='a' and ch<='z':
            lower=True
        
        if ch>='A' and ch<='Z':
            upper=True
            
        if ch>='0' and ch<='9':
            number=True
            
        elif ch in string.punctuation:
            special=True
            
    if lower and upper and number and special:
        return True
    
    return False

#encoding password
def encode_password(password):
    
    encode = hashlib.sha512(password.encode("utf-8")).hexdigest()
    return encode

#generating password
def generate_password():

    while True:
        
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        special_char = random.choice(string.punctuation)
        number = str(random.randint(1,100))
        
        password = adjective + noun + special_char + number
        
        if check(password):
            print(f"the generated password: {password}, is strong!\n")
        else:
            print(f"the generated password: {password}, is weak!\n")
            
        choice=input("do you want another password? (y/n): ")
        
        if choice == "n":
            return password
    
#check user
def add_user():
    new_user = input("\nenter a user name: ")
    while new_user in users:
        print()
        if new_user in users:
            print("user already exists, try another")
        new_user = input("enter a user name: ")

    users.append(new_user)
    
    print("\nuser registered successfully!\n")
    print("Please select a passwrod from below:")
    
    password = generate_password()
    
    encode = encode_password(password)
    
    users.append(new_user)
    passwords.append(encode)
    recent_password=password
    
    data[new_user] = encode
    
    print("\nRegistration Successfull!")
    print("\n\n",new_user,recent_password,encode,"\n\n")
    
def login():   
    
    count = 0
    
    while True:
        user = input("enter username: ")
        if user not in users:
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
        encode = encode_password(password)
        print(password,encode,"\n")
        if encode in passwords:
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
    
    
add_user()
login()