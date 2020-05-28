#!/usr/bin/python3

arquivo = open('arquivo.csv') # Abertura para leitura do arquivo
dados = arquivo.read() # Leitura do arquivo
arquivo.close() # fechamento do arquivo

# splitlines quebra as linha usando um delimitador
for registro in dados.splitlines():
    print('Nome: {}, idade: {}'.format(*registro.split(',')))

'''
O * representa os argumentos variaveis
'''