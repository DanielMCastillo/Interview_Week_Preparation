#!/bin/python3
#sum min max
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    sumarray = sum(arr)
    minim = min(arr)
    maxim = max(arr)

    print(str(sumarray - maxim) + " " + str(sumarray - minim))
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
