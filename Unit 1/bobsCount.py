#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:39:19 2022

@author: Aazath
"""
'''
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
first = 0
last =3
bobCount = 0
for i in range(len(s)-1):
    if(s[first:last] =='bob'):
        bobCount +=1
    first +=1
    last +=1
print('Number of times bob occurs is :',bobCount)