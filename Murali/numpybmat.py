#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/numpy-bmat-python/
    
'''

# Import necessary modules
# numpy.rot90() method 

# Python Program illustrating 
# numpy.bmat 

import numpy as geek 
def startpy():
    A = geek.mat('4 1; 22 1') 
    B = geek.mat('5 2; 5 2') 
    C = geek.mat('8 4; 6 6') 

    # array like igeekut 
    a = geek.bmat([[A, B], [C, A]]) 
    print("Via bmat array like input : \n", a, "\n\n") 

    # string like igeekut 
    s = geek.bmat('A, B; A, A') 
    print("Via bmat string like input : \n", s)

if __name__ == '__main__':
    startpy()
