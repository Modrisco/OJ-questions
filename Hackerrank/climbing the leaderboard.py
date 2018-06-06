#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rank = []
    scores_set = sorted(list(set(scores)))
    i = 0
    j = 0
    while i < len(alice) and j < len(scores_set):
        if alice[i] < scores_set[j]:
            rank.append(len(scores_set) - j + 1)
            i += 1
        elif alice[i] == scores_set[j]:
            rank.append(len(scores_set) - j)
            i += 1
            j += 1
        elif alice[i] > scores_set[j]:
            j += 1
            if alice[i] > scores_set[-1]:
                rank.append(1)
                i += 1
    while i < len(alice):
        rank.append(1)
        i += 1
    return rank
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
