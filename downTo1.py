# -*- coding: utf-8 -*-
"""
11/30/2022

Anthony Mak
"""

def even(num):
    num = num // 2
    return num

def odd(num):
    num = 3 * num + 1
    return num

numIn = 5

while numIn < 21:
    evenOdd = numIn % 2
    numRes = numIn
    numSteps = 0
    while numRes != 1:
        if evenOdd == 0:
            numRes = even(numRes)
        else:
            numRes = odd(numRes)
            numSteps += 1
        evenOdd = numRes % 2
    print (f'Starting at {numIn},took {numSteps} steps to reach 1')
    numIn += 1
        
