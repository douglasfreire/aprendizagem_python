from random import randint
'''
randint: função responsavel por gerar um valor aleatorio entre 
um numero inteiro inicial e um numero inteiro final
'''

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero: '))

print(f'Numero secreto {numero_secreto} foi encontrado')