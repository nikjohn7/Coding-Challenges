#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    m=max(arr)
    res=[0]*(m+1)
    for i in range(len(arr)):
        res[arr[i]]+=1
    ans=[]
    for i in range(len(res)):
        if res[i]>0:
            temp=[i]*res[i]
            ans.extend(temp)
    return ans

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))

