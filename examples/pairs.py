#!/bin/python3

import math
import os
import random
import re
import sys

import time


# from itertools import combinations

# Complete the pairs function below.
def pairs(k, arr):
    arr=sorted(arr)
    count=0
    # two pointer approach
    i=0;j=i+1
    n=len(arr)
    print(n)
    while j<n and i<n:
        diff=arr[j]-arr[i]
        if diff==k:
            count+=1
            j+=1
        elif diff<k:
            j+=1
        else:
            i+=1
    return count

    # combination approach; affected with time out
    # for x,y in combinations(arr,2):
    #     if abs(x-y)==k:
    #         count+=1
    # return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    st_time=time.time()

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(str(result) + '\n')

    print("Time taken: ",st_time-time.time())
