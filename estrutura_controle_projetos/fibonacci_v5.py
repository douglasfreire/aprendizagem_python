#!/usr/bin/python3

'''
Gerar uma quantidade de numero na sequencia de Fibonacci
'''
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(resultado[-2] + resultado[-1])
        if len(resultado) == quantidade:
            break
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib)