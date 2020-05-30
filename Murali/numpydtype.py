#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: krish
Source: https://www.geeksforgeeks.org/data-type-object-dtype-numpy-python/
    
'''
# Python Program to create a data type object 
# containing a 32 bit big-endian integer 
import numpy as np

def startpy():

    # i4 represents integer of size 4 byte 
    # > represents big-endian byte ordering and < represents little-endian encoding. 
    # dt is a dtype object 
    dt = np.dtype('>i4') 

    print("Byte order is:",dt.byteorder) 

    print("Size is:",dt.itemsize) 

    print("Data type is:",dt.name)

if __name__ == '__main__':
    startpy()


