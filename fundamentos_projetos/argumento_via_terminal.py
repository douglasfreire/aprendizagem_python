import math
import sys

def circulo(raio):
    return math.pi * float(raio) ** 2


def help():
    print( f'''\
        É necessário informar o raio do circulo.
        Sintaxe: python {sys.argv[0]} <valor do raio>
    ''')
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()        
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo: ', area)

'''
    Para Executar esse script, passar o valor no final
    python argumento_via_terminal 12.4
'''