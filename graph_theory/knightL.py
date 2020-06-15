#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import product
from collections import deque

def bfs(s, e,a,b,n):
    """
    function for bfs traversal of the graph
    :param: G for graph as dict
    :s: int for start node
    """
    # root node is said to have 0 depth
    # in case of tree
    depth=1
    pathLen=-1
    visited=set()
    nQueue=deque()

    nQueue.append([s,depth])
    visited.add(s)

    # to iterate through whole nodes
    while len(nQueue)>0:
        # in case depth is not required
        #v,_=nQueue.popleft()
        v,r=nQueue.popleft()

        # iterating over all the neighbours of the node
        # in inspection
        for _n in getNeighbours(v,a,b,n):
            # if neighbour node is not visited
            # then visit it
            if _n not in visited:
                nQueue.append([_n,r+1])
                visited.add(_n)
            if _n==e:
                # end is met
                # breaking all the iterations
                pathLen=r
                nQueue.clear()
                break
                #' to add extra functionality
    return pathLen

def getNeighbours(p,a,b,n):
    steps=[]
    if (p[0]+a)<n and (p[1]+b)<n:
        steps.extend([(p[0]+a,p[1]+b)])
    if (p[0]+b)<n and (p[1]+a)<n:
        steps.extend([(p[0]+b,p[1]+a)])
    
    if (p[0]-a)>=0 and (p[1]+b)<n:
        steps.extend([(p[0]-a,p[1]+b)])
    if (p[0]-b)>=0 and (p[1]+a)<n:
        steps.extend([(p[0]-b,p[1]+a)])
    
    if (p[0]-a)>=0 and (p[1]-b)>=0:
        steps.extend([(p[0]-a,p[1]-b)])
    if (p[0]-b)>=0 and (p[1]-a)>=0:
        steps.extend([(p[0]-b,p[1]-a)])
    
    if (p[0]+a)<n and (p[1]-b)>=0:
        steps.extend([(p[0]+a,p[1]-b)])
    if (p[0]+b)<n and (p[1]-a)>=0:
        steps.extend([(p[0]+b,p[1]-a)])
    
    return steps

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    # changing steps on each iterations
    startP=(0,0)
    endP=(n-1,n-1)

    t_list=[]
    for _i in range(1,n):
        tmpList=[]
        for _j in range(1,n):
            tmpList.append(bfs(startP, endP, _i,_j,n))
        t_list.append(tmpList)
    
    return t_list

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')

    # fptr.close()
