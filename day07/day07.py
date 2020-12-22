#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:29:12 2020

@author: utkuburgaz
"""
import re

# Read Inputs
f = open("input", "r")
inputs = f.read().splitlines()

# Prepare Data

def splitter(inputs:list):
    t = []
    for i in inputs:
        v = re.split(" contain |, ",i)
        t.append(v)
    return t

def sterilizer(inputs:list):
    k = []
    
    for j in inputs:
        t = []
        for i in j:
            i = i.replace(' bags','').replace('.','').replace(' bag', '')
            t.append(i)
        k.append(t)
    for n in k:
        for m in range(len(n)):
            if m == 0:
                n[m]=n[m].replace(' ', '_')
            else:
                n[m]=n[m].split(' ',1)
                n[m][1]=n[m][1].replace(' ', '_')
                if n[m][0] != 'no':
                    n[m][0]=int(n[m][0])
                else:
                    n[m][0]=0
    return k

def dictionary(inputs:list):
    k = inputs
    d = {}
    for n in range(len(k)):
        e = {}
        for m in range(1,len(k[n])):
            key = k[n][m][1]
            value = k[n][m][0]
            e[key] = value
        d[k[n][0]] = e    
        del e
    return d
        

splitted = splitter(inputs)

sterilized = sterilizer(splitted)

dictionary = dictionary(sterilized)



# Day 7 - Part 1

def searchbags(color:str, rules:list, counter=0, k={}):
    for i in rules:
        if color in rules[i]:
            counter+=1
            k[i]=1
            searchbags(i, rules, counter, k)
    return len(k)


print(searchbags('shiny_gold', dictionary))


# Day 7 - Part 2

def seachnested(color, rules, counter=0):
    if color in rules:
        for i in rules[color]:
            counter+=rules[color][i] + rules[color][i]*seachnested(i, rules)
    return counter


print(seachnested('shiny_gold', dictionary))