#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import product, combinations
from collections import Counter

def deviation(l):
    l=sorted(l)
    return sum([l[x+1]-l[x]-1 for x in range(len(l)-1)])

# Complete the steadyGene function below.
def steadyGene(gene):
    positions=dict()
    eachAllowedLength=len(gene)//4
    c={k:v-eachAllowedLength for k,v in Counter(gene).items() if (v-eachAllowedLength)>0}
    windowSize=sum(c.values())

    for k in c.keys():
        positions[k]=[i for i,x in enumerate(gene) if x==k]
    # exact combination is missing
    # if we need to remove 4 C and 1 T, it should find deviation having 4 C and 1 T
    # not just 5 removables

    # create the combinations

    for _i in product(*[combinations(positions[k], c[k]) for k in c.keys()]):
        print(_i)
    return None

    # return min([deviation(dl[i:i+windowSize]) for i in range(len(dl)-windowSize+1)])+windowSize

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
