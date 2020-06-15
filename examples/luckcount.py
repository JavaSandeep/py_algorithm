#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
from itertools import product

## GET NEIGHBOURS FUNCTION
## USE FOR GRID
def getNeighbours(p,n):
    """
    p is the current index
    n is the size of n*n grid
    works only for square grid
    """
    a,b=1,1
    row,col=n
    steps=[]
    
    if (p[0]+a)<row:
        steps.extend([(p[0]+a,p[1])])
    
    if (p[1]+b)<col:
        steps.extend([(p[0],p[1]+b)])
    
    if (p[0]-a)>=0:
        steps.extend([(p[0]-a,p[1])])
    
    if (p[1]-b)>=0:
        steps.extend([(p[0],p[1]-b)])
    
    return list(set(steps))
## ENDS


## BFS starts
def bfs(Grid, s, e='*'):
    """
    function for bfs traversal of the graph
    :param: G for graph as dict
    :s: int for start node
    """
    # root node is said to have 0 depth
    # in case of tree
    wandcast=0
    depth=0

    childToParent=dict()
    pathsDown=dict()

    visited=set()
    nQueue=deque()
    endPoint=None
    nQueue.append([s,depth])
    visited.add(s)

    # to iterate through whole nodes
    while len(nQueue)>0:
        # in case depth is not required
        #v,_=nQueue.popleft()
        v,r=nQueue.popleft()

        # iterating over all the neighbours of the node
        # in inspection
        neighbours=[(x,y) for x,y in getNeighbours(v,(len(Grid),len(Grid[0]))) if Grid[x][y]!='X' and ((x,y) not in visited)] # Removing trees
        # print(neighbours)
        for _n in neighbours:
            # if neighbour node is not visited
            # then visit it
            pathsDown[v]=neighbours
            if _n not in visited:
                childToParent[_n]=v
                nQueue.append([_n,r+1])
                visited.add(_n)
            if Grid[int(_n[0])][int(_n[1])]==e:
                endPoint=(int(_n[0]),int(_n[1]))
                nQueue.clear()
                break
    
    # start with the ending
    pathTored=[endPoint]
    parent=endPoint
    while True:
        parent=childToParent.get(parent)
        pathTored.append(parent)
        if parent==s:
            break
    
    for each in pathTored:
        if len(pathsDown.get(each,[]))>=2:
            wandcast+=1

    return wandcast
        #' to add extra functionality
## BFS ENDS

# Complete the countLuck function below.
def countLuck(matrix, k):
    start=None
    for x,y in product(range(len(matrix)), range(len(matrix[0]))):
        if matrix[x][y]=='M':
            start=(x,y)
            break
    # print(bfs(matrix, start), k)
    if bfs(matrix, start)==k:
        return 'Impressed'
    else:
        return 'Oops!'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        print(result + '\n')

    # fptr.close()
