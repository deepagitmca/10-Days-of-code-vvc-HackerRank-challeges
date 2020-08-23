#!/bin/python

import math
import os
import random
import re
import sys

def move(i, j, n):
    def move1(i, j, v, x):
        g = []
        for k in v:
            h = [[k[0]+i, k[1]+j],[k[0]+i, k[1]-j],[k[0]-i, k[1]+j],[k[0]-i, k[1]-j],[k[0]+j, k[1]+i],[k[0]+j, k[1]-i],[k[0]-j, k[1]+i],[k[0]-j, k[1]-i]]
            for z in h:
                if z[0] < 0 or z[1] < 0:
                    pass
                else:
                    try:
                        if not x[z[0]][z[1]]:
                            x[z[0]][z[1]] = 1
                            g.append(z)
                    except: pass
        return(g, x)

    x = []
    for z in range(n):
        x.append([0] * (n))
    x[0][0] = 1
    v = [[0, 0]]
    p = 0
    while v:
        v, x = move1(i, j, v, x)
        p += 1
        if x[-1][-1]:
            return(p)
    return(-1)

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    l = []
    t = n-1
    for i in range(t):
        l.append([0] * (t))
    l[0][0] = t
    l[-1][-1] = 1
    l[0][-1] = t * 2 if t % 2 == 0 else t
    l[-1][0] = l[0][-1]
    for i in range(1, t-1):
        l[i][i] = t//(i+1) if t % (i+1) == 0 else -1
        if t % (i+1) == 0:
            l[i][-1] = 2 * (t//(i+1)) if (t//(i+1)) % 2 == 0 else (t//(i+1))
        else: l[i][-1] = -1
        l[-1][i] = l[i][-1]
        for j in range(i):
            u = move(i+1, j+1, n)
            l[i][j] = u
            l[j][i] = u
    return(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
