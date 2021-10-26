#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def findDecentDigits(n, fives):
    if n < 3:
        return 0, 0
    if n % 3 == 0:
        n = 0
        return n, fives
    else:
        fives -= 5
        n -= 5
        return findDecentDigits(n, fives)

def decentNumber(n):
    # Write your code here
    threes = 0
    fives = n
    threes, fives = findDecentDigits(n, fives)
    return threes, fives

def decentNumber(n):
    org = n
    fives = 0
    threes = n
    while n >= 3:
        if n % 3 == 0:
            break
        else:
            n -= 5
    
    fives = n
    threes -= fives
    if threes % 5 != 0 or fives % 3 != 0:
        threes, fives = 0, 0
    
    theDecentNumber = "5" * fives + "3" * threes
    print(org, threes, fives)
    return int(theDecentNumber) if len(theDecentNumber) > 0 else -1

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))

# tests = [x for x in range(1, 12)]
# for test in tests:
#     print(decentNumber(test))