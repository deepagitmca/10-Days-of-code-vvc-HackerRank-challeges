#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    stack1, stack2, stack3 = sum(h1),sum(h2),sum(h3)
    temp1,temp2,temp3 = h1.copy(),h2.copy(),h3.copy()

    while not(stack1 == stack2 == stack3):
        if stack1 == max([stack1,stack2,stack3]):
            stack1 -= temp1.pop(0)
            continue
        if stack2 == max([stack1,stack2,stack3]):
            stack2 -= temp2.pop(0)
            continue
        if stack3 == max([stack1,stack2,stack3]):
            stack3 -= temp3.pop(0)
            continue
    return stack3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

