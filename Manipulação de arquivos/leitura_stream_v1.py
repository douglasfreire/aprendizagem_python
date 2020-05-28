#!/usr/bin/python3

'''
Nesse tipo de leitura ao inves dele ler o arquivo todo e guardar dentro de uma vairiavel,
ele vai lendo o arquivo por partes e trazendo o resultado aos poucos
'''
arquivo = open('arquivo.csv')
for registro in arquivo:
    print('Nome: {}, idade: {}'.format(*registro.split(',')))
arquivo.close()
