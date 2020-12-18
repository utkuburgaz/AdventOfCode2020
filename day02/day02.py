#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:24:35 2020

@author: utkuburgaz
"""

# Read Inputs
f = open("input", "r")
inputs = f.read().splitlines()

# Sterilize Data
def sterilize(i):
    i = i.split(" ")
    i[1] = i[1].replace(":","")
    i[0] = list(map(int, i[0].split("-")))
    return i

inputs = list(map(sterilize, inputs))


# Day 2 - Part 1
counter = 0
for i in inputs:
    repeat = i[2].count(i[1])
    if repeat in range(i[0][0], i[0][1]+1):
        counter+=1
        
print(counter)



# Day 2 - Part 2
counter = 0
for i in inputs:
    char = i[1]
    pos1 = i[0][0]
    pos2 = i[0][1]
    # XOR
    if bool(i[2][pos1-1] == char) ^ bool(i[2][pos2-1] == char):
        counter+=1
        
print(counter)