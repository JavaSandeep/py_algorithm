#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations

# Complete the minimumLoss function below.
def minimumLoss(price):
    minP=min(price)
    if minP>1:
        price=[x-(minP-1) for x in price]
    # print(price)
    return min([x-y for x,y in combinations(price,2) if x-y>0])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    print(str(result) + '\n')

    # fptr.close()
