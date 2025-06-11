#Busqueda por interpolacion
#complejidad O(log log n)
def busqueda_interpolacion(lista,objetivo):
    inicio = 0
    fin = len(lista) -1
    
    while inicio <= fin and lista[inicio] <= objetivo <= lista[fin]:
        pos = inicio + ((objetivo - lista[inicio]) * (fin - inicio)) // (lista[fin] - lista[inicio])

        if lista[pos] == objetivo:
            return pos
        elif lista[pos] < objetivo:
            inicio = pos + 1
        else:
            fin = pos - 1

    return -1