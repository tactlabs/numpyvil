#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/numpy-cos-python/
    
'''

# Import necessary modules
# numpy.flip() method 

# Python program explaining 
# cos() function 

import numpy as np 
import math 

def startpy():
    in_array = [0, math.pi / 2, np.pi / 3, np.pi] 
    print ("Input array : \n", in_array) 

    cos_Values = np.cos(in_array) 
    print ("\nCosine values : \n", cos_Values)


if __name__ == '__main__':
    startpy()
