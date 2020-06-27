#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#
from collections import deque

weightMap=dict()
visited=set()
nQueue=deque()

def bfs(G, s, blocked_node):
    """
    function for bfs traversal of the graph
    :param: G for graph as dict
    :s: int for start node
    """
    # root node is said to have 0 depth
    # in case of tree
    visited.clear()
    nQueue.clear()

    nQueue.append(s)
    visited.add(s)

    # start with first start node weight
    weight=weightMap.get(s)

    # to iterate through whole nodes
    while len(nQueue)>0:
        # in case depth is not required
        #v,_=nQueue.popleft()
        v=nQueue.popleft()

        # iterating over all the neighbours of the node
        # in inspection
        for _n in G.get(v):
            # if neighbour node is not visited
            # then visit it
            if (_n not in visited) and _n!=blocked_node:
                nQueue.append(_n)
                visited.add(_n)
                weight+=weightMap.get(_n)
                #' to add extra functionality

    return weight

def setGraph(nCount, edges):
    """
    Fastest method to set graph
    returns graph
    :param: nCount number of nodes in graph - n nodes
    :param: edges list of edges in graph
    """
    # setting the nodes
    g=dict()

    for _t,_e in edges:
        if _t not in g.keys():
            g[_t]=[_e]
        else:
            g[_t].append(_e)
        if _e not in g.keys():
            g[_e]=[_t]
        else:
            g[_e].append(_t)
    
    g.update({k:[] for k in range(1,nCount+1) if k not in g.keys()})
    
    return g

def cutTheTree(data, edges):
    # Write your code here
    weightMap.update({k+1:v for k,v in enumerate(data)})
    G=setGraph(len(data),edges)
    minNode=float('inf')
    for nodeS,nodeE in edges:
        # copy the graph
        # G=deepcopy(gGraph)
        # G.get(nodeS).remove(nodeE)
        # G.get(nodeE).remove(nodeS)
        # to remove
        minNode=min(minNode, abs(bfs(G,nodeE,nodeS)-bfs(G,nodeS,nodeE)))
    # remove each edge from edges
    # calculating sum and comparing
    # let's use simple bfs
    return minNode

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
