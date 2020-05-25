#!/usr/bin/python3

'''
Recursividade utlizando o operador ternario
com if
'''

def fibonacci(quantidade, sequencia=(0, 1)):
    # Condição de parada
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == "__main__":
    # Listar os 20 ṕrimeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib)
        