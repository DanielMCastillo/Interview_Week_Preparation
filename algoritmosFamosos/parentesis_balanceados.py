#balanceo de parentesis
def balanceoSimbolos(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expresion:
        if char in "([{":
            pila.append(char)
        elif char in ")]}":
            if not pila or pila[-1] != pares[char]:
                return False
            pila.pop()
    return len(pila) == 0


print(balanceoSimbolos("([{}])"))   # True
print(balanceoSimbolos("(([])"))    # False
print(balanceoSimbolos("{[()]}"))   # True
print(balanceoSimbolos("{[}]"))     # False