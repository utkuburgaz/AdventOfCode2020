#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:48:14 2020

@author: utkuburgaz
"""
from itertools import combinations 

# Read Inputs
f = open("input", "r")
inputs = list(map(int, f.read().splitlines()))


# Day 1 - Part 1 
for i in range(len(inputs)):
    expense = inputs[i]
    remain = 2020 - expense
    if remain in inputs:
        print(remain * expense)
        break

# Day 1 - Part 2
comb = combinations(inputs,3)

for i in comb:
    if i[0]+i[1]+i[2] == 2020:
        print(i[0]*i[1]*i[2])