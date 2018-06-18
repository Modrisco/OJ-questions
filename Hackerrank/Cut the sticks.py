#!/bin/python3
# https://www.hackerrank.com/challenges/cut-the-sticks/problem
import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    sticks_left = []
    while len(arr) > 0:
        sticks_left.append(len(arr))
        arr = list(filter(lambda a: a != 0, [e-min(arr) for e in arr]))
    return sticks_left

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
