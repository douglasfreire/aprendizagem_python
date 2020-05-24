#!/usr/bin/python3

'''
Nessa versão será utilizado uma lista
no lugar das variaveis
'''
def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        # Aqui o penultimo receberá o valor do ultimo e o ultimo receberá o valor do penultimo + ultimo
        resultado.append(resultado[-2] + resultado[-1])
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(100):
        print(fib)