#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 18:17:35 2020

@author: utkuburgaz
"""

# Read Inputs
f = open("input", "r")
inputs = f.read().splitlines()

# Day 5 - Part 1
maksid = 0
for j in inputs:
    rows = [0,127]
    seats = [0,7]
    for i in j:
        if i == 'F':
            rows[1] = rows[1]-(rows[1]-rows[0]+1)/2
        if i == 'B':
            rows[0] = rows[0]+(rows[1]-rows[0]+1)/2
        if rows[0] == rows[1]:
            row = rows[0]
        if i == 'L':
            seats[1] = seats[1]-(seats[1]-seats[0]+1)/2
        if i == 'R':
            seats[0] = seats[0]+(seats[1]-seats[0]+1)/2
        if seats[0] == seats[1]:
            seat = seats[0]
    seatid = int(row*8)+int(seat)
    if seatid > maksid:
        maksid = seatid

print(maksid)



# Day 5 - Part 2

occupancy = []
for j in inputs:
    rows = [0,127]
    seats = [0,7]
    for i in j:
        if i == 'F':
            rows[1] = rows[1]-(rows[1]-rows[0]+1)/2
        if i == 'B':
            rows[0] = rows[0]+(rows[1]-rows[0]+1)/2
        if rows[0] == rows[1]:
            row = rows[0]
        if i == 'L':
            seats[1] = seats[1]-(seats[1]-seats[0]+1)/2
        if i == 'R':
            seats[0] = seats[0]+(seats[1]-seats[0]+1)/2
        if seats[0] == seats[1]:
            seat = seats[0]
    seatid = int(row*8)+int(seat)
    occupancy.append(seatid)
    occupancy.sort()

for k in occupancy:
    if k+1 not in occupancy and k+2 in occupancy:
        print(k+1)