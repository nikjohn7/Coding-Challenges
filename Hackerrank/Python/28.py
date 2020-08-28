#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count=0
    p_initial=p
    p+=d
    while s>=0:
        if (s-p<0 and count>0) or (s<p_initial and count==0):
            break
        if p>m:
            if p-d>m:
                p-=d
            else:
                p=m
        s-=p
        count+=1
        print(s,p,count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
