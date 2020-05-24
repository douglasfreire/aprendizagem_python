#!/usr/bin/python3

'''
Gerar uma quantidade de numero na sequencia de Fibonacci utilizando o for
'''
def fibonacci(quantidade):
    resultado = [0, 1]
    # O uso do underline indica que uma variavel n usada. É uma boa pratica na comunidade.
    for _ in range(2, quantidade):
        resultado.append(resultado[-2] + resultado[-1])
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib)