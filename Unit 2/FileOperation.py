#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:47:21 2022

@author: Aazath
"""

nameFile = open('names','w')
for i in range(2):
    name = input('What is your Name ?: ')
    nameFile.write(name + '\n')
nameFile.close()

nameHandler = open('names','r')
for line in nameHandler:
    print('Name is : '+line)
nameHandler.close()



