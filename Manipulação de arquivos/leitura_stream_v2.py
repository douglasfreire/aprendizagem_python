#!/usr/bin/python3

'''
Nesse tipo de leitura ao inves dele ler o arquivo todo e guardar dentro de uma vairiavel,
ele vai lendo o arquivo por partes e trazendo o resultado aos poucos

strip para eliminar os espaços
'''
arquivo = open('arquivo.csv')
for registro in arquivo:
    print('Nome: {}, idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
