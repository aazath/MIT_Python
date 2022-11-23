#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:53:10 2022

@author: Aazath
"""

# def quotion_and_remainder(x,y):
#     q = x//y
#     r = x%y
#     return(q,r)

# print(quotion_and_remainder(10, 20))
def get_date(aTuple):
    nums =()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


(small, large, words) = get_date(((1, 'mine'),
                                  (3, 'yours'),
                                  (5, 'ours'),
                                  (7, 'mine'))) 

print(small, large, words)




