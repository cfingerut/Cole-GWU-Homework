# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:21:56 2020

@author: cfing
"""
contn = 'y'


start_number = 0


while contn == 'y':
    
    user_number = int(input("How many numbers?"))
    
    for i in range(start_number, user_number+start_number):
        print(i)
    
    start_number = start_number+user_number
        
    contn = input("Do you want to continue? 'y'/'n'")