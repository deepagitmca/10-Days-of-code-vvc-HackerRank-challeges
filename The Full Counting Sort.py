#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    a=[]
    b=len(arr)
    for i in range(len(arr)):
        a.append(int(arr[i][0]))
    c = max(a)  
    d=[[] for _ in range(c+1)]
    for j in range(b):
        g=arr[j]
        h=int(g[0])
        k=g[1]
        if(j<(b/2)):
            d[h].append('-')
        else:
            d[h].append(k)
    p=''
    for i in range(c+1):
        g=''
        for j in range(len(d[i])):
            g+=d[i][j]
            g+=' '
        p+=g
    print(p)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
