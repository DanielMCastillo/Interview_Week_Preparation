#Busqueda lineal
#Complejidad O(n) - lenta en listas grandes
def busqueda_lineal(lista,objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    
    return -1

#probando
numeros = [1,3,5,7,9,11,13,15]
objetivo = 7

resultado = busqueda_lineal(numeros,objetivo)
if resultado!=-1:
    print(f"Elemento encontrado en el indice{resultado}")
else:
    print("Elemento no encontrado")
    