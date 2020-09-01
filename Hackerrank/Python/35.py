#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    if len(w)==1:
        return 1
    w.sort()
    count=1
    mins=w[0]
    for i in w[1:]:
        if i>mins+4:
            count+=1
            mins=i
    return count

if __name__ == '__main__':

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)
    print(str(result) + '\n')

