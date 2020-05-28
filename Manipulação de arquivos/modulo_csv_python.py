import csv

'''
Esse modulo do python facilita a manipulação de
arquivos csv
'''

with open('arquivo.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, idade: {}'.format(*pessoa))