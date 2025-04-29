#!/bin/python3
# This is a sample Python script.
#Print the following  lines, each to  decimals:
#proportion of positive values
#proportion of negative values
#proportion of zeros

import math
import os
import random
import re
import sys

def plusMinus(arr):
    positivos = 0
    negativos = 0
    zeros = 0
    # Write your code here
    for i in arr:
        if i >0:
            positivos +=1
        elif i<0:
            negativos+=1
        else:
            zeros +=1
            
            
    positives = positivos/len(arr)
    negatives = negativos/len(arr)  
    ceros = zeros/len(arr)
    print(positives)
    print(negatives)
    print(ceros)
    
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

