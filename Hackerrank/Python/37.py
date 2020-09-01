#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(pile):
    if len(pile)==1:
        return 'First'
    res=pile[0]
    for i in pile[1:]:
        res^=i
    if res==0:
        return 'Second'
    else:
        return 'First'

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        print(result)

