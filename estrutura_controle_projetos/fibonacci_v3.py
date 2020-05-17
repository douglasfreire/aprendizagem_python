#!/usr/bin/python3

'''
Nessa versão será implementado o packing para trocar variaveis
'''
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=', ')

    while ultimo < limite:
        # Aqui o penultimo receberá o valor do ultimo e o ultimo receberá o valor do penultimo + ultimo
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=', ')


if __name__ == '__main__':
    fibonacci(100)