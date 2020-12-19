#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:15:37 2020

@author: utkuburgaz
"""
import re

# Read Inputs
f = open("input", "r")
inputs = re.split("\n\n",f.read())

# Sterilize Data to Make a List of Dicts

sterilized = []
for i in inputs:
    psprt = re.split('\n| ', i)
    temp = {} 
    for j in psprt :
        v = re.split(':', j)
        if len(v) >= 2:  
            temp[v[0]] = v[1]
    sterilized.append(temp)


# Day 4 - Part 1
mustfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
counter = 0

for i in sterilized:
    fcount = 0
    for field in mustfields:
        if field in i:
            fcount+=1
    if fcount == 7:
        counter+=1

print(counter)



# Day 4 - Part 2
mustfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

byr = {'name': 'byr', 'must':1, 'min':1920, 'max':2002}
iyr = {'name': 'iyr', 'must':1, 'min':2010, 'max':2020}
eyr = {'name': 'eyr', 'must':1, 'digit':4, 'min':2020, 'max':2030}
hgt = {'name': 'hgt', 'must':1, 'min_in':59, 'max_in':76, 'min_cm':150, 'max_cm':193}
hcl = {'name': 'hcl', 'must':1, 'regex':'^#[0-9a-f]{6}$'}
ecl = {'name': 'ecl', 'must':1, 'color':['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']}
pid = {'name': 'pid', 'must':1, 'digit':9}
cid = {'name': 'cid', 'must':0}

fields = {'byr':byr, 'iyr':iyr, 'eyr':eyr, 'hgt':hgt, 'hcl':hcl, 'ecl':ecl, 
          'pid':pid, 'cid':cid}
          

counter = 0

for i in sterilized:
    fcount = 0
    check = True
    for field in mustfields:
        if field in i:
            fcount+=1
    if fcount == 7:
        # BYR
        if int(i[fields['byr']['name']])<fields['byr']['min'] or int(i[fields['byr']['name']])>fields['byr']['max']:
            check = False

        #IYR
        if int(i[fields['iyr']['name']])<fields['iyr']['min'] or int(i[fields['iyr']['name']])>fields['iyr']['max']:
            check = False

        #EYR
        if int(i[fields['eyr']['name']])<fields['eyr']['min'] or int(i[fields['eyr']['name']])>fields['eyr']['max']:
            check = False

        #ECL
        if i[fields['ecl']['name']] not in fields['ecl']['color']:
            check = False

        #PID
        if len(i[fields['pid']['name']]) != fields['pid']['digit']:
            check = False

        #HGT
        if "in" in i[fields['hgt']['name']]:
            if int(i[fields['hgt']['name']].replace("in", ""))<fields['hgt']['min_in'] or int(i[fields['hgt']['name']].replace("in", ""))>fields['hgt']['max_in']:
                check = False   
        elif "cm" in i[fields['hgt']['name']]:
            if int(i[fields['hgt']['name']].replace("cm", ""))<fields['hgt']['min_cm'] or int(i[fields['hgt']['name']].replace("cm", ""))>fields['hgt']['max_cm']:
                check = False
        else:
            check = False
        
        #HCL
        if not re.match(fields['hcl']['regex'], i[fields['hcl']['name']]):
            check = False
      
        if check == True:
            counter+=1
            

print(counter)

        
