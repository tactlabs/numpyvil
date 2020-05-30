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

import numpy
import perfplot

def startpy():
    perfplot.show(
    setup=lambda n: numpy.random.rand(n),
    kernels=[
        lambda a: numpy.r_[a, a],
        lambda a: numpy.stack([a, a]).reshape(-1),
        lambda a: numpy.hstack([a, a]),
        lambda a: numpy.concatenate([a, a])
        ],
    labels=['r_', 'stack+reshape', 'hstack', 'concatenate'],
    n_range=[2**k for k in range(19)],
    xlabel='len(a)',
    logx=True,
    logy=True,
    )


if __name__ == '__main__':
    startpy()