#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:59:36 2020

@author: utkuburgaz
"""
import re

# Read Inputs
f = open("input", "r")
inputs = re.split("\n\n",f.read())

sterilized = []
for i in inputs:
    sterilized.append(re.split("\n",i))
    

# Day 6 - Part 1
sums = 0
for i in sterilized:
    v = []
    for j in i:
        for k in j:
            if k not in v:
                v.append(k)
    sums+=len(v)
    
print(sums)



# Day 6 - Part 2
def sumed(t,l):
    count = 0
    for i in t:
        if t[i] == l:
            count+=1
    return count

sums = 0
ans = {}
for i in sterilized:
    v = []
    ans = {}
    for j in i:
        for k in j:
            if k not in ans:
                ans[k]=1
            else:
                ans[k]+=1
    sums+=sumed(ans, len(i))

print(sums)