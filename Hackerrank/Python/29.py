#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    pages=dict()
    count=0
    page=1
    for i in arr:
        j=1
        while True:
            if j+k<i+1:
                if page in range(j,j+k):
                    count+=1
                j+=k
            else:
                if page in range(j, i+1):
                    count+=1
                break
            page+=1
        page+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
