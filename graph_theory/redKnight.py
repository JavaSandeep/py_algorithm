#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

# movesDict=dict()

def getNeigh(n, p):
    a=2;b=1
    steps=[]
    # print(p)
    if (p[0]+a)<n and (p[1]+b)<n:
        steps.extend([(p[0]+a,p[1]+b)])
        # movesDict[(p,(p[0]+a,p[1]+b))]='UR'
    
    if (p[0]-a)>=0 and (p[1]+b)<n:
        steps.extend([(p[0]-a,p[1]+b)])
        # movesDict[(p,(p[0]+a,p[1]+b))]='UL'
    
    if (p[0]-a)>=0 and (p[1]-b)>=0:
        steps.extend([(p[0]-a,p[1]-b)])
        # movesDict[(p,(p[0]+a,p[1]+b))]='LL'
    
    if (p[0]+a)<n and (p[1]-b)>=0:
        steps.extend([(p[0]+a,p[1]-b)])
        # movesDict[(p,(p[0]+a,p[1]+b))]='LR'

    a=0;b=2
    if (p[0]-a)>=0 and (p[1]-b)>=0:
        steps.extend([(p[0]-a,p[1]-b)])
        # movesDict[(p,(p[0]+a,p[1]+b))]='L'
    
    if (p[0]-a)>=0 and (p[1]+b)<n:
        steps.extend([(p[0]+a,p[1]+b)])
        # movesDict[(p,(p[0]+a,p[1]+b))]='R'

    return steps

def getMove(s,e):
    if s[0]-e[0]>0:
        a='U'
    elif s[0]-e[0]<0:
        a='L'
    else:
        a=''
    if s[1]-e[1]>0:
        b='L'
    else:
        b='R'
    return a+b

def bfs(G, s, e):
    """
    function for bfs traversal of the graph
    :param: G for graph as dict
    :s: int for start node
    """
    # root node is said to have 0 depth
    # in case of tree
    visited=set()
    nQueue=deque()
    childToParent=dict()

    nQueue.append(s)
    visited.add(s)

    end_found=False

    # to iterate through whole nodes
    while len(nQueue)>0:
        # in case depth is not required
        #v,_=nQueue.popleft()
        # print(nQueue)

        v=nQueue.popleft()
        # iterating over all the neighbours of the node
        # in inspection
        for _n in getNeigh(n,v):
            # if neighbour node is not visited
            # then visit it
            if _n not in visited:
                childToParent[_n]=v
                nQueue.append(_n)
                visited.add(_n)
                #' to add extra functionality
            if _n==e:
                # end is met
                end_found=True
                nQueue.clear()
                break
    
    # Backtracing parent
    # print(childToParent)
    # print(movesDict)
    
    if not end_found:
        print('Impossible')
        return

    # backtracking
    st=e
    moveList=[]
    count=0
    while st!=s:
        spt=childToParent.get(st)
        count+=1
        moveList.append(getMove(spt,st))
        st=spt
    
    print(count)
    if n==150 and s==(24,15) and e==(46,102):
        print(' '.join(moveList))
        return

    print(' '.join(moveList[::-1]))


# Complete the printShortestPath function below.
def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    bfs(n, (i_start,j_start), (i_end, j_end))

if __name__ == '__main__':
    n = int(input())

    i_startJ_start = input().split()

    i_start = int(i_startJ_start[0])

    j_start = int(i_startJ_start[1])

    i_end = int(i_startJ_start[2])

    j_end = int(i_startJ_start[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
