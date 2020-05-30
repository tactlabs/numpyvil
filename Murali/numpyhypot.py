#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/numpy-hypot-python/
    
'''

# Import necessary modules


# Python3 program explaining 
# hypot() function 

import numpy as np 
def startpy():

    leg1 = [12, 3, 4, 6] 
    print ("leg1 array : ", leg1) 


    leg2 = [5, 4, 3, 8] 
    print ("leg2 array : ", leg2) 

    result = np.hypot(leg1, leg2) 
    print("\nHypotenuse is as follows :") 
    print(result) 

if __name__ == '__main__':
    startpy()
