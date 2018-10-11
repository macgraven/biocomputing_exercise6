#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:21:23 2018

@author: Mac
"""

def headPython(file_name, n):
    result = []
    nlines=0
    assert n >=1
    for line in open(file_name):
        result.append(line)
        nlines+=1
        if nlines >= n:
            break
    return result
print(headPython('wages.csv',5))