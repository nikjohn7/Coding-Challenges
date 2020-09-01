#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    n=len(sticks)
    sticks.sort()
    k=n-3
    while k>=0 and (sticks[k]+sticks[k+1]<=sticks[k+2]):
        k-=1
    if k>=0:
        return [sticks[k],sticks[k+1],sticks[k+2]]
    else:
        return [-1]
if __name__ == '__main__':

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(' '.join(map(str, result)))
    print('\n')

