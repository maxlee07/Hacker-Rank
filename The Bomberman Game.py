#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
def fullgrid(r,c):
    lst=[]
    for i in range(r):
        t=[]
        for j in range(c):
            t.append("O")
        lst.append(t)
    return lst

def explosion(grid,r,c):
    f_grid=fullgrid(r,c)
    for i in range(r):
        for j in range(c):
            if grid[i][j]=="O":
                f_grid[i][j]="."
                if i+1<r:
                    f_grid[i+1][j]="."
                if i-1>-1:
                    f_grid[i-1][j]="."
                if j+1<c:
                    f_grid[i][j+1]="."
                if j-1>-1:
                    f_grid[i][j-1]="."
    return f_grid

def bomberMan(n, grid):
    # Write your code here
    #print(grid[1][3])
    if n==1:
        return grid
    elif n%2==0:
        lst=fullgrid(len(grid),len(grid[0]))
        return ["".join(x) for x in lst]

    else:
        i=2
        while i<=n:
            if i%2!=0:
                print(i)
                grid=explosion(grid,len(grid),len(grid[0]))
            i+=1
    
    return ["".join(x) for x in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
