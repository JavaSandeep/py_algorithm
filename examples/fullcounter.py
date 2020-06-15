#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    sortMap=dict()
    counter=0
    halfWay=len(arr)//2
    for idx,val in arr:
        if idx not in sortMap.keys():
            sortMap[idx]=[]
        # Change the string upto half length
        if counter<=halfWay:
            val='-'
        sortMap[idx].append(val)

    strArray=[]
    for i in range(max(map(int, sortMap.keys()))+1):
        if str(i) in sortMap.keys():
            strArray.extend(sortMap.get(str(i)))
    
    return ''.join(strArray)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
