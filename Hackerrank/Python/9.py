import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d=dict()
    for i in magazine:
        if i in d: 
            d[i] = d[i] + 1
        else: 
            d[i] = 1
    for i in note:
        if i in d:
            if d[i]==0:
                print ('No')
                return
            d[i]-=1
        else:
            print('No')
            return
    print('Yes')




if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)