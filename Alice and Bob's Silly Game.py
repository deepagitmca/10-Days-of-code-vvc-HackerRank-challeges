#!/bin/python3

import os
import sys

#
# Complete the sillyGame function below.
#

b = [2] 

def prime(a):
        for i in range(2, int(a ** .5) + 1):
            if not a % i: return False
        return True

def sillyGame(n):
    #
    # Write your code here.
    #
    c = b[-1]
    if n > c:
        for i in range(c + 1, n + 1):
            if prime(i): b.append(i)
    return 'Alice' if sum(i <= n for i in b) % 2 else 'Bob'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        result = sillyGame(n)

        fptr.write(result + '\n')

    fptr.close()
