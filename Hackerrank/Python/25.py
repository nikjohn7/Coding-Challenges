#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    shift=0
    for i in range(1,len(arr)):
        curr=arr[i]
        j=i-1
        while j>=0 and curr<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            shift+=1
        arr[j+1]=curr
    return shift
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
