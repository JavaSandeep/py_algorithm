#!/bin/python3

import math
import os
import random
import re
import sys

from queue import LifoQueue
from collections import deque

# 1,2,3,4,5,6
# 1,5,4,3,2,6
# 0,3,1,-1,-3,0
# 1,5,3,4,2,6
# 0,3,0,0,-3,0
# 1,5,6,3,2,4
# 0,3,3,-1,-3,2

# 1,2,3,4,5
# 5,4,3,2,1
# 4,2,0,-2,-4

# Complete the almostSorted function below.
def almostSorted(arr):
    diffarr=[x-y for x,y in zip(arr,sorted(arr))]
    # condensing data
    allsyms=[(i+1,x) for i,x in enumerate(diffarr) if x!=0]
    print(allsyms)
    if len(allsyms)==2:
        # only swapping can do it
        idx,_=zip(*allsyms)
        return "yes\nswap {0} {1}".format(*sorted(idx))
    
    # # check for continuity
    # if not all([True if (allsyms[x+1][0]-allsyms[x][0])==1 else False for x in range(len(allsyms)-1)]):
    #     return "no"

    # for rearranging the non negative deviations
    # must have even length
    if not(len(allsyms)%2):
        # qSet=LifoQueue()
        qSet=deque()
        #TODO: Requires enhancments
        # test for reversibility
        # enqueue and dequeue can occur only once
        # for the half of the queue it must enqueue
        # and for other half it must dequeue
        for _,val in allsyms[:len(allsyms)//2]:
            if val>0:
                qSet.append(val)

        for _,val in allsyms[len(allsyms)//2:]:
            if val<0 and qSet[-1]==(-1*val):
                qSet.pop()

        if not qSet:
            # the series is reversible
            idx,_=zip(*allsyms)
            return "yes\nreverse {0} {1}".format(min(idx),max(idx))

    return "no"


    


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(almostSorted(arr))