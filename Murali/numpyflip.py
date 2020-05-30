#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/numpy-flip-python/
    
'''

# Import necessary modules
# numpy.flip() method 

import numpy as geek 

def startpy():  
    array = geek.arange(8).reshape((2,2,2)) 
    print("Original array : \n", array) 
  
    print("Flipped array : \n", geek.flip(array, 0))  

if __name__ == '__main__':
    startpy()
