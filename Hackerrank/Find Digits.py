#!/bin/python3
# https://www.hackerrank.com/challenges/find-digits/problem
import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    divisors = 0
    divided = list(map(int, str(n)))
    for i in range(len(divided)):
        if divided[i] != 0:
            if n % divided[i] == 0:
                divisors += 1
    return divisors

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
