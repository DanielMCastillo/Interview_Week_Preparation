#Es una estructura de datos tipo LIFO (Last In, First Out), es decir, el último elemento en entrar es el primero en salir.
#Operaciones: push() (agregar), pop() (eliminar), peek() (ver el primer elemento).

stack = []
stack.append(1)  # push
stack.append(2)  # push
stack.append(3)  # push
print(stack.pop())  # pop -> 3
