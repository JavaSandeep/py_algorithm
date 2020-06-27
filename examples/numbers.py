#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
from collections import Counter
from itertools import combinations

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def nonDivisibleSubset(k, s):
    if k==1:
        return k
    # Write your code here
    c_map=Counter([x%k for x in s])
    # neutralizing boundaries
    # for key,v in c_map.items():
    #     boundry=gcm(int(key),k)//int(key)
    #     if v>=boundry:
    #         c_map[key]=boundry-1
    # Handling the zero condition
    totalLen=0
    # attmptlist=list(map(int, c_map.keys()))
    # attmptlist2=[x for x in c_map if x and x<=(k//2)]
    # needs cross breeding
    valSet=set()
    tmpList=[x for x in list(map(int, c_map.keys())) if x]
    for x in sorted(tmpList):
        key=x;antikey=(k-x)

        # boundary cndn
        if key==antikey:
            boundry=lcm(int(key),k)//int(key)
            if c_map[key]>=boundry:
                c_map[key]=boundry-1

        if c_map.get(key,-1)>=c_map.get(antikey,-1):
            sp_key=key
        else:
            sp_key=antikey

        if (k-sp_key) not in valSet:
            valSet.add(sp_key)

    for key in valSet:
        totalLen+=c_map.get(key)
    
    if 0 in c_map.keys():
        totalLen+=1
    
    return totalLen
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(str(result) + '\n')

    # fptr.close()
