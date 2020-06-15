#!/bin/python3

import math
import os
import random
import re
import sys
import time


from itertools import product

# Complete the surfaceArea function below.
def surfaceArea(A):
    # Create objects
    totalArea=0
    for x,y in product(range(len(A)),range(len(A[0]))):
        height=A[x][y]
        faceArea=2
        # All the cross neighbours of a cell in matrix
        sideFaceArea=0
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            try:
                if x+dx<0 or y+dy<0:
                    raise Exception()
                neighbour=A[x+dx][y+dy] # raises exception if could not access the index
            except Exception:
                neighbour=0
            
            # will be skipped if index not found
            # print(height,neighbour, max(0,height-neighbour))
            sideFaceArea+=max(0,height-neighbour)

        # print("Surface Area {0} {1} {2}".format(x,y,faceArea+sideFaceArea))
        totalArea+=(faceArea+sideFaceArea)
    return totalArea

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    starttime=time.time()
    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(result)
    print("Total time taken: ",time.time()-starttime)

    # fptr.write(str(result) + '\n')

    # fptr.close()
