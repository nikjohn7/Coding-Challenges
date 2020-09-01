#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    counts=dict(Counter(s))
    vals=list(counts.values())
    if len(s)%2==0:
        for i in vals:
            if i%2==1:
                return 'NO'
        return 'YES'
    else:
        cnt_odd=0
        for i in vals:
            if i%2==1:
                cnt_odd+=1
        if cnt_odd==1:
            return 'YES'
        else:
            return 'NO'





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
