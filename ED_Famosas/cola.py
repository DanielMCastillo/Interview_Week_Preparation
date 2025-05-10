#Definición: Es una estructura de datos tipo FIFO (First In, First Out), es decir, el primer elemento en entrar es el primero en salir.
#Operaciones: enqueue() (agregar), dequeue() (eliminar), front() (ver el primer elemento).
queue = []
queue.append(1)  # enqueue
queue.append(2)  # enqueue
queue.append(3)  # enqueue
print(queue.pop(0))  # dequeue -> 1
