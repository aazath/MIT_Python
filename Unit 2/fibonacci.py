#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:20:15 2022

@author: Aazath
"""

def fib(x):
    """assume x an int >= 0
    return fibonacci of x"""
    if x==1 or x==0:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    

