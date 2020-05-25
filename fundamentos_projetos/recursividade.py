'''
Recursividade é um metodo que chama ele mesmo. 
É importante que exista um metodo de parada.
'''

def imprimir(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    imprimir(maximo, atual +1)

imprimir(10, 1)
