'''
Created on Dec 30, 2016

@author: wans
'''

import math


def cal_entropy(p_list):
    tot = 0
    for p in p_list: 
        tot +=-1*p *math.log2(p)
    return tot

print(cal_entropy([1/3, 2/3]))
