#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    counts=list(Counter(arr).items())
    counts.sort(reverse=True, key=lambda x:x[1])
    top=counts[0]
    dels=0
    for key in counts[1:]:
        dels+=key[1]
    return dels



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
