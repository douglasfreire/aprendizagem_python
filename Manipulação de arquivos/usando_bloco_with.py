#!/usr/bin/python3

'''
Usando o with garante o fechamento do recurso alocado dentro
do bloco
'''

with open('arquivo.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, idade: {}'.format(*registro.strip().split(',')))


if arquivo.closed:
    print("Verificando se o arquivo foi fechado mesmo")