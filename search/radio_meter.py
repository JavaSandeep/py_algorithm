#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters2(x, k):
    hLoc=[i if i in x else -1 for i in range(min(x),max(x)+1)]
    # hLoc=sorted(x)
    # start from 0th position
    # to check pos = 0+k
    # can we locate antena at  pos
    # if yes install radio
    # if no to check pos = to check pos -1
    # after install jump to installed_pos+k+1
    # # check if it's house yes repeat same process
    # # else increase by 1
    antenna=0
    start_pos=0
    while start_pos < len(hLoc):
        if hLoc[start_pos]==-1:
            start_pos+=1
            continue
        print("Start pos: ",start_pos," start house: ",hLoc[start_pos])
        is_installed=False
        to_install=start_pos+k
        # boundary check
        # if to_install
        # backtracking mechanism
        while not is_installed:
            if to_install < len(hLoc) and hLoc[to_install]!=-1:
                antenna+=1
                # start pos check is not done here
                # start pos has to be valid
                print("Antenna installed at pos: ",to_install, " installed house: ",hLoc[to_install])
                start_pos=to_install+k+1
                is_installed=True
            else:
                to_install-=1
    return antenna

def hackerlandRadioTransmitters(x, k):
    # hLoc=[i if i in x else -1 for i in range(min(x),max(x)+1)]
    hLoc=sorted(list(set(x)))
    antenna=0
    start_pos=0
    # print(hLoc)
    while start_pos < len(hLoc):
        antenahouse=max([y for y in hLoc[start_pos:start_pos+k+1] if hLoc[start_pos]<=y<=hLoc[start_pos]+k])
        antenna+=1
        incr=0
        # coverage house or next start house
        h=antenahouse+k
        if h < hLoc[-1]:
            cv_house=min([y for y in hLoc[start_pos:] if y>=h])
            if cv_house==h:
                incr=1
        else:
            cv_house=hLoc[-1]
            incr=1
        start_pos=hLoc.index(cv_house)+incr
        # print(antenahouse, cv_house, hLoc[start_pos], incr, hLoc[hLoc.index(cv_house)], hLoc[start_pos])
    return antenna

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    # result = hackerlandRadioTransmitters2(x, k)
    result = hackerlandRadioTransmitters(x, k)

    print(str(result) + '\n')

    # fptr.close()
