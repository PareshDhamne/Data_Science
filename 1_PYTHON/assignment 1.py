# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:49:17 2023

@author: Hp
"""
#1)find BMI by using height and weight
height = float(input("Enter the height in m:"))
weight = float(input("Enter the weight in kg:"))
BMI = round((weight/(height*height)),2)
if BMI < 18.5:
    print(f"Your weight is under weight and BMI is:{BMI}")
elif BMI > 18.5 and BMI < 25:
    print(f"Your weight is normal and BMI is:{BMI}")
elif BMI > 25 and BMI < 30:
    print(f"Your weight is over and BMI is:{BMI}")
elif BMI > 30 and BMI < 35:
    print(f"Your weight is obese and BMI is:{BMI}")
elif BMI > 35:
    print(f"Your weight is uinically obese and BMI is:{BMI}")


#2)Write a python code using logical operators and if, elif, so as to allow for roller coster also ask user age and charge ticket accordingly>
print("Welcome to the roller coster ride")
height = int(input("Enter the height in cm:"))
if height >= 120:
    print("You are eligible for ride.")
    age = int(input("Enter your age in years:"))
    bill = 0
    if age <= 12:
        print("Tickit for child is 5$")
        bill += 5
    elif age > 12 and age <= 18:
        print("Tickit for youth is 7$")
        bill += 7
    elif age > 18 and age <= 45:
        print("Tickit for young is 12$")
        bill += 12
    elif age > 45:
        print("Tickit for Adults is 50$")
        bill += 50
    photo =input("you want photo Y or N:")
    if(photo=='Y'):
        bill+=3
        print("Your total bill is:",bill)
    else:
        print("Your bill is:",bill)
else:
    print("You are not eligible for ride.")
        
        
