#!/usr/bin/python3

'''
Na função open() o primeiro atributo é o file e o segundo o mode onde se coloca
o o tipo de alteração. Nesse caso o w significa escrita.
'''

with open('arquivo.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, idade: {}'.format(*pessoa), file=saida)


if arquivo.closed:
    print("Verificando se o arquivo foi fechado mesmo")


if saida.closed:
    print("Verificando se o arquivo foi fechado mesmo")