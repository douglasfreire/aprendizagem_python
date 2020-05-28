#!/usr/bin/python3

'''
Usando o try / finally posso garantir que ao abrir o arquivo 
eu posso fecha-lo mesmo que ocorra algum erro na execução. O finally sempre será
executado.
'''

try:
    arquivo = open('arquivo.csv')
    for registro in arquivo:
        print('Nome: {}, idade: {}'.format(*registro.strip().split(',')))

finally:
    arquivo.close()