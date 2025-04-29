#!/bin/python3
#manually median
#using numpy
#np.median(arr)

import math
import os
import random
import re
import sys

def findMedian(arr):
    # Write your code here
    arregloordenado = sorted(arr)
    n = len(arr) 
    mitad = n//2
    print(mitad)
    
    if n % 2 == 0:
        return (arregloordenado[mitad - 1] + arregloordenado[mitad]) / 2
    else:
        return arregloordenado[mitad]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
