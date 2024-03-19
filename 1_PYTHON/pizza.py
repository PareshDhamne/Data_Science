# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:26:38 2023

@author: Hp
"""

def make_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")