#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/numpy-divide-python/
    
'''

# Python program explaining 
# divide() function 
import numpy as np 

def startpy():

    # input_array 
    arr1 = [2, 27, 2, 21, 23] 
    arr2 = [2, 3, 4, 5, 6] 
    print ("arr1		 : ", arr1) 
    print ("arr2		 : ", arr2) 

    # output_array 
    out = np.divide(arr1, arr2) 
    print ("\nOutput array : \n", out) 

if __name__ == '__main__':
    startpy()
