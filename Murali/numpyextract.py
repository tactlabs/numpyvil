#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/numpy-extract-python/
    
'''
# Python Program illustrating 
# numpy.compress method 

import numpy as geek 

def startpy():
    array = geek.arange(10).reshape(5, 2) 
    print("Original array : \n", array) 

    a = geek.mod(array, 4) !=0
    # This will show element status of satisfying condition 
    print("\nArray Condition a : \n", a) 

    # This will return elements that satisy condition "a" condition 
    print("\nElements that satisfy condition a : \n", geek.extract(a, array)) 



    b = array - 4 == 1
    # This will show element status of satisfying condition 
    print("\nArray Condition b : \n", b) 

    # This will return elements that satisy condition "b" condition 
    print("\nElements that satisfy condition b : \n", geek.extract(b, array)) 

if __name__ == '__main__':
    startpy()