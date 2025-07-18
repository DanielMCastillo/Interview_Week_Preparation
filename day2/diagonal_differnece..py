#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    diag1 = sum(arr[i][i] for i in range(n))
    diag2 = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(diag1 - diag2)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
