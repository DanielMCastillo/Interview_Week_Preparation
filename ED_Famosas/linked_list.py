#lista enlazada
#Definición: Es una estructura de datos en la que cada elemento (nodo) contiene un valor y una referencia (enlace) al siguiente nodo.
#Operaciones: insert() (insertar), delete() (eliminar), traverse() (recorrer).
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        
            
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.traverse()  # 3 -> 2 -> 1 -> None
