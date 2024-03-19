# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:46:53 2023

@author: Hp
"""

#1)check whether the given string is anagram or not
#anagram is a method in which with the help of one string we caan get other string with same lenth and letters
def anagram(str1,str2):
    #here we are using .lower function to check whether in given strings any space or other is given or not
    a=list(str1.replace(""," ").lower())
    b=list(str2.replace(""," ").lower())
    if(len(a)!=len(b)):
        return False
    else:
        return (sorted(a)==sorted(b))
print(anagram("elbow","below"))

#2)add the number in the list which are divisible by 5 or 7

lst = [1,5,7,10,35,14,32,67,70,45]
def return_sum(lst):
    sum=0
    for i in range(len(lst)):
        if(lst[i]%5==0 or lst[i]%7==0):
            sum=sum+lst[i]
    return sum
print(return_sum(lst))


#write a function to revrse word in a sentence.
def rev(input):
    #if string is empty
    if input=="":
        print("No output")
    else:
        convert=input.split()
        reverse=" ".join(reversed(convert))
    return reverse
c = input("Enter the string:")
print(rev(c))