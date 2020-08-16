import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def minimumSwaps(arr):
    count=0
    n=len(arr)
    diction={}
    arr=[x-1 for x in arr]
    for ind, elem in enumerate(arr):
        diction[elem] = ind
    visited = [False] * n
    for elem, ind in sorted(diction.items(), key=lambda x: x[0]):
        if visited[elem] or elem == ind:
            continue
        cycles = 0
        i = elem
        while not visited[i]:
            visited[i] = True
            i = diction[i]
            cycles += 1
        count += cycles - 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()