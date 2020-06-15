#!/bin/python3

import time
import math
import os
import random
import sys
from collections import deque

def bfs(G, s, search_depth=None):
    """
    function for bfs traversal of the graph
    :param: G for graph as dict
    :s: int for start node
    """
    # root node is said to have 0 depth
    # in case of tree
    depth=0

    visited=set()
    nQueue=deque()

    # freeing up memory
    visited.clear()
    nQueue.clear()

    nQueue.append([s,depth])
    visited.add(s)

    # to iterate through whole nodes
    while len(nQueue)>0:
        # in case depth is not required
        #v,_=nQueue.popleft()
        v,r=nQueue.popleft()

        # searching upto fix depth
        # search_depth=None for full depth search
        # do for only unvisited node
        # None and 0 has same effect
        # very hard to catch
        # print(visited)
        if (search_depth is not None) and r >= search_depth:
            continue

        # iterating over all the neighbours of the node
        # in inspection
        for _n in G.get(v):
            # if neighbour node is not visited
            # then visit it
            if _n not in visited:
                nQueue.append([_n,r+1])
                visited.add(_n)
                #' to add extra functionality
        
    return visited

def bfsUtil(G,s,all_nodes):
    city_vis=set()
    is_optimal=True
    for s_city,strenght in s:
        # print("City and strenght: ",s_city,strenght)
        g_ret=bfs(G,s_city,strenght)
        # print(g_ret, city_vis)
        if (city_vis & g_ret):
            is_optimal=False
            break
        city_vis=city_vis | g_ret
    
    if city_vis!=all_nodes:
        is_optimal=False
    
    return is_optimal

def setGraph(nCount, edges):
    """
    Optimal function to set graph without weights
            without directions
    :params: nCount -> number of nodes
    :params: edges -> edges connecting the nodes
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

# Complete the prims function below.
def akhbar(n, e, s):
    gGraph=setGraph(n,e)
    a_n=set(range(1,n+1))

    res=bfsUtil(gGraph, s, a_n)
    if res:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = int(input().strip())

    for _ in range(nt):
        starttime=time.time()
        edges=[]
        soldiers=[]
        
        n,r,m=map(int, input().strip().split())

        for _ in range(r):
            edges.append(list(map(int, input().strip().split())))
        
        for _ in range(m):
            soldiers.append(list(map(int, input().strip().split())))
        
        result=akhbar(n, edges, soldiers)

        print(result)
        print("Time taken: ",time.time()-starttime)
        # print("\n\n")
