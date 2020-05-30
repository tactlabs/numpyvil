#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source:
    
'''

# Import necessary modules
import numpy as np

def startpy():
    a = np.array([
        [1, 2, 4],
        [11, 22, 34],
        [2, 5, 7]
    ])
    a.shape
    b = np.array([
        [19, 18, 16],
        [9, -2, -14],
        [18, 15, 13]
    ])
    b.shape
    c = np.concatenate((a, b))
    print(c)


if __name__ == '__main__':
    startpy()