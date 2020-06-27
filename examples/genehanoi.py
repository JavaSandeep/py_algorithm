#!/bin/python3

import math
import os
import random
import re
import sys

# towerOfHanoi for 4 pegs
def towerOfHanoi(n, from_rod, to_rod, aux_rod1, aux_rod2): 
    if (n == 0): 
        return
    if (n == 1): 
        print("Move disk", n, "from rod", from_rod, "c to rod",  to_rod) 
        return
      
    towerOfHanoi(n - 2, from_rod, aux_rod1, aux_rod2, to_rod) 
    print("Move disk", n-1, "from rod", from_rod, "c to rod", aux_rod2) 
                  
    print("Move disk", n, "from rod", from_rod, "c to rod", to_rod)
    print("Move disk", n-1, "from rod", aux_rod2, "c to rod", to_rod) 
              
    towerOfHanoi(n - 2, aux_rod1, to_rod, from_rod, aux_rod2) 

def restoreTower(state):
    
    pass

if __name__ == '__main__':
    N = int(input())

    a = list(map(int, input().rstrip().split()))

    print(restoreTower(a))
