#!/bin/python3

import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
from itertools import product
from math import factorial
from collections import Counter

def ncr(N,r):
    return factorial(N)/(factorial(r)*factorial(N-r))

def is_anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return True
    else:
        return False

def sherlockAndAnagrams(s):
    count = []

    # word length to match on each iteration
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = list({k:v for k,v in Counter(a).items() if v>1}.values())
        tmpcount=[ncr(_j,2) for _j in b]
        count.append(sum(tmpcount))
    return int(sum(count))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
