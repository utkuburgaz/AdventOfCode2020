#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:51:54 2020

@author: utkuburgaz
"""
import re

# Read Inputs
f = open("input", "r")

def splitter(inputs:list):
    t = []
    for i in inputs:
        v = re.split(" ",i)
        t.append([v[0], int(v[1])])
    return t

inputs = splitter(f.read().splitlines())




# Day 8 - Part 1

ids = []
i = 0 
acc = 0
while i not in ids:
    ids.append(i)
    if inputs[i][0] == 'acc' :
        acc+=inputs[i][1]
        i+=1
    elif inputs[i][0] == 'jmp':
        jmp = inputs[i][1]
        i+=jmp
    else:
        i+=1
    
print(acc)



# Day 8 - Part 2

def change(k:list):
    if k[0] == 'jmp':
        k[0] = 'nop'
    elif k[0] == 'nop':
        k[0] = 'jmp'
    return k


def find():
    for j in inputs:
        j = change(j)
        i = 0 
        ids = []
        acc = 0
        while i not in ids:
            ids.append(i)
            if i == len(inputs):
                return acc
            #print(i,"=>",inputs[i])
            if inputs[i][0] == 'acc' :
                acc+=inputs[i][1]
                i+=1
                #print("acc: ",acc,"i =>",i)
            elif inputs[i][0] == 'jmp':
                jmp = inputs[i][1]
                i+=jmp
                #print("jmp: ",jmp,"i =>",i)
            else:
                i+=1
        j = change(j)


print(find())

    


