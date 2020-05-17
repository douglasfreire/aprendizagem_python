import math

'''
Para importar uma função de um modulo:
    * nome_do_modulo.nome_da_função()
    * from nome_do_modulo import nome_da_função
'''


def circulo(raio):
    print('Área do círculo: ', math.pi * float(raio) ** 2 )

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
    