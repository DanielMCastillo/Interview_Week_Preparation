#!/bin/python3
#valor unico
import math
import os
import random
import re
import sys

def lonelyinteger(a):
    # Write your code here
    return [i for i in set(a)if a.count(i)==1].pop()
    # usando funcion set
    #set devuelve un conjunto de elementos unicos
    #pop devuelve el primer elemento del conjunto
    #count devuelve el numero de veces que aparece un elemento en la lista
    #en este caso el elemento que aparece una sola vez
    #NOTA: HAY QUE AGREGAR POP() PARA QUE DEVUELVA UN SOLO ELEMENTO

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
