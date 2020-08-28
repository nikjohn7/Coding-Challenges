#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the acmTeam function below.
def acmTeam(topic):
    ans=defaultdict(int)
    for i in range(len(topic)-1):
        for j in range(i+1, len(topic)):
            res=bin(topic[i] | topic[j]).count('1')
            ans[res]+=1
    m=max(list(ans.keys()))
    print(ans)
    return [m, ans[m]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = int('0b'+input(),2)
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
