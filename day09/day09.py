#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 21:43:30 2020

@author: utkuburgaz
"""
from itertools import combinations

with open('input') as file:
    inputs = [int(i) for i in file.read().splitlines()]
    


# Day 9 - Part 1

def combsum(comb):
    sums = set()
    for t in comb:
        sums.add(t[0] + t[1])
    return sums
       
def notpermable(perm, inputs):
    for i in range(perm, len(inputs)):
        comb = list(combinations(inputs[i-perm:i],2))
        num = inputs[i]
        if num not in combsum(comb):
            return num
       
print(notpermable(25, inputs))
   

# Day 9 - Part 2
        
def contiguous(num, inputs):
    cont = []
    for i in inputs:
        if i < num:
            if sum(cont)<num:
                cont.append(i)
                
            while sum(cont)>num:
                cont.pop(0)
                
            if sum(cont) == num:
                cont.sort()
                return cont[0]+cont[-1]

       
print(contiguous(167829540, inputs))