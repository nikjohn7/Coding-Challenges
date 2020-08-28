#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    mini=float('inf')
    if len(a)==len(set(a)):
        return -1
    info=dict()
    for i,ele in enumerate(a):
        if ele in info:
            newdist=i-info[ele][1]
            info[ele][0]=newdist
            if newdist>0 and newdist<mini:
                mini=newdist
            info[ele][1]=i
        else:
            info[ele]=[0,i]
    return mini

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
