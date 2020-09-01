#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the luckBalance function below.
def luckBalance(k, contests):
    imp=[]
    other=[]
    tot=0
    for i in contests:
        if i[1]==1:
            imp.append(i[0])
        else:
            other.append(i[0])
    heapq.heapify(imp)
    while len(imp)-k>0:
        a=heapq.heappop(imp)
        tot-=a
    return tot+sum(imp)+sum(other)

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(str(result) + '\n')

