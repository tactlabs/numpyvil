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
        [1, 2],
        [3, 4]
    ])
    inverse_a = np.linalg.inv(a)
    print(inverse_a)


if __name__ == '__main__':
    startpy()