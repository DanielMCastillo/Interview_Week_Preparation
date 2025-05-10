#palindromos
#verificar si es un palindromo
def esPalindromo(cadena):
    limpio = ''.join(i for i in cadena if i.isalnum()).lower()
    return limpio == limpio[::-1]

print(esPalindromo("Hola Mundo"))
print(esPalindromo("OSO"))

    