#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:38:39 2022

@author: apple
"""

# def gcd(a, b):
#     '''
#     a, b: two positive integers
#     returns the greatest common divisor of a & b.
#     '''
#     while a != 0:
#         (a, b) = (b, a % b)
#     return a

def gcd(a, b):
    """
    a, b: two positive integers

    Returns the greatest common divisor of a & b.
    """
    if b == 0:
        return a

    # Recursive case
    return gcd(b, a % b)