#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:12:53 2020

@author: utkuburgaz
"""

# Read Inputs
f = open("input", "r")
inputs = f.read().splitlines()

trees = list()


# Manipulate Data
for i in inputs:
    rows = list()
    for j in i:
        if j == "#":
            rows.append(1)
        else:
            rows.append(0)
    trees.append(rows)
    

# Day 3 - Part 1
counter, i, j = 0 ,0, 0

while i < len(trees):
    if trees[i][j%len(trees[0])]:
        counter+=1
    i += 1
    j += 3
    
print(counter)


# Day 3 - Part 2
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
temp = 1
for k in slopes:
    counter, i, j = 0, 0, 0
    while i < len(trees):
        if trees[i][j%len(trees[0])]:
            counter+=1
        i += k[1]
        j += k[0]
    counter=temp*counter
    temp = counter
    
print(counter)

        
        
        