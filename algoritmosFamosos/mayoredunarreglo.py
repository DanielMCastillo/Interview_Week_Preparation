#mayor de un array
numeros =[1,2,3,4,5]
mayor = max(numeros)
print(mayor)

#manual
numeros2 = [1,44,8,10,2]
mayor2 = numeros2[0]
for numero in numeros2:
    if numero>mayor2:
        mayor2 = numero

print(mayor2)
