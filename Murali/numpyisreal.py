#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/numpy-isrealobj-python/
    
'''
# Python program explaining 
# isrealobj() function 
import numpy as np 

def startpy():
    in_array = [1, 3, 5, 4] 
    print ("Input array : ", in_array) 

    output_value = np.isrealobj(in_array) 
    print ("\nIs real : ", output_value) 

if __name__ == '__main__':
    startpy()
