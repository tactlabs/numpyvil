#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/numpy-rot90-python/
    
'''

# Import necessary modules
# numpy.rot90() method 

import numpy as np 

def startpy():
    array = np.arange(12).reshape(3, 4) 
    print("Original array : \n", array) 

    # Rotating array 4 times : Returns same original array 
    print("\nArray being rotated 4 times : \n", np.rot90(array, 4)) 

    # Rotating once 
    print("\nRotated array : \n", np.rot90(array)) 

    # Rotating twice 
    print("\nRotated array : \n", np.rot90(array, 2)) 


if __name__ == '__main__':
    startpy()
