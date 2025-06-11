#binary search Oracle Interview Algorithm
#Complejidad O(log n) - Rapido pero debe estar ordenada la lista
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1 
    while inicio <= fin:
        medio = (inicio+fin)//2
        valor_medio = lista[medio]
        
        if valor_medio == objetivo:
            return medio #El indice donde se encuentre el objetivo
        elif valor_medio < objetivo:
            inicio = medio+1 #buscar en la mitad derecha
        else:
            fin = medio-1 #Buscar en la mitad izquierda
        
    return -1 #Si no se encuentra el objetivo


#Ejemplo de uso
numeros = [1,3,5,7,9,11,13,15]
objetivo = 7

resultado = busqueda_binaria(numeros,objetivo)
if resultado!=-1:
    print(f"Elemento encontrado en el indice{resultado}")
else:
    print("Elemento no encontrado")
    