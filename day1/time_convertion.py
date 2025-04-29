#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def timeConversion(s):
    hh, mm , ss = map(int, s[:-2].split(":"))
    if s[-2:] == 'AM' and hh == 12:
        hh = 0
    elif s[-2:] == 'PM' and hh != 12:
        hh+=12

    return f"{hh:02}:{mm:02}:{ss:02}"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
