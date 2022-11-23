#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:42:34 2022

@author: Aazath
"""

import math
def polysum(n,s):
    '''
    Input: n - number of sides(an integer value grater than 0)
    s- length of each sides(can be an intger or a float)
    
    Output: Returns Sum of area and the square of the perimeter of the regular polygon(float value)
    '''
    # method to calculate the area
    def areaOfPolygon(n,s):
        #Pi = 3.1428
        area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return area
    
    # method to calculate the perimeter
    def perimeterOfPolygon(n,s):
        perimeter = n * s
        return perimeter
    sum = areaOfPolygon(n,s) + (perimeterOfPolygon(n,s) ** 2)
    return round(sum,4)