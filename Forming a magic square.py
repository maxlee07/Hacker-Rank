#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
#check if the matric is magic square
import itertools
def ismagic(s):
    const=15
    #row check:
    for i in s:
        x=sum(i)
        if x!=const:
            return False
    #column check:
    for i in range(len(s)):
        x=0
        for j in range(len(s)):
            x+=s[j][i]
        if x!=const:
            return False
    #diagnol check:
    x=0
    y=0
    for i in range(len(s)):
        x+=s[i][i]
        y+=s[2-i][i]
    if x!=const or y!=const:
            return False
    return True
def minmumcost(s,c):
    cost=0
    for i in range(len(s)):
        for j in range(len(s)):
            cost+=abs(s[i][j]-c[i][j])
    return cost

def formingMagicSquare(s):
    # Write your code here
    imax=100
    if ismagic(s):
        return 0
    
    #genrate all the posible 3*3 matric in inclusive range [1,9]
    N = 3
    for seq in itertools.permutations(range(1, N*N+1)):
        # Split the sequence into a candidate magic square,
        #   N rows of N elements each.
        cand = [seq[i:i+N] for i in range(0, N*N, N)]
        if ismagic(cand):
            imax=min(imax,minmumcost(s,cand))
        
    return imax
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
