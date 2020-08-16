import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    maxm=-63
    sums=[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            sums.append((sum(arr[i][j:j+3]))+(sum(arr[i+2][j:j+3]))+arr[i+1][j+1])
    print (max(sums))