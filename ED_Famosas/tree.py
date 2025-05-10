#Arbol binario
#Definición: Es una estructura jerárquica de datos compuesta por nodos, donde cada nodo tiene un valor y referencias a nodos hijos. Un tipo común es el árbol binario.
#Operaciones: insert() (insertar), delete() (eliminar), traverse() (recorrer en orden).

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def traverse(self, node):
        if node:
            self.traverse(node.left)
            print(node.value, end=" ")
            self.traverse(node.right)

bt = BinaryTree(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.traverse(bt.root)  # 2 3 4 5 7
