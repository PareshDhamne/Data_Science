# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:59:00 2023

@author: Hp
"""

users = ["admin",'Employee',"manager","worker","staff"]
for user in users:
    if user=='admin':
        print('Hello admin,would you like to see a status report:')
    elif user=='Employee':
        print("Hello Employee")
    elif user=='manager':
        print("Hello manager")
    elif user=='worker':
        print("Hello Worker")
    elif user=='staff':
        print("Hello staff")
    else:
        print("Hello")
        
current_users=['ali','ahemad','fahad','aun','rana']
new_users=['ali','rana','bilal','huzi','dula']
for new_user in new_users:
    if new_user in current_users:
        print("Person will need to enter a new username.")
    else:
        print("Saying that the username is available.. ")
        

import hashlib
hashlib.sha512("PaRESH@02".encode('utf-8')).hexdigest()
'25d6335293b45ece72afed5c79513c0943ff6f8772ac09d51066e381213dee26f3780e47e070cbf0d5628bac87e55c7759e9ba5d389d17a815c06c314c6abc19'
len(hashlib.sha512("PaRESH@02".encode('utf-8')).hexdigest())
        
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
