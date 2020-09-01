import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    price=dict()
    for i,ele in enumerate(arr):
        if ele<m:
            if m-ele in price:
                return sorted([i+1, price[m-ele]+1])
            price[ele]=i

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(' '.join(map(str, result)))