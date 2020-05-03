import math
import sys
import errno


class TerminalColor():
    ERRO = '\033[91m'
    NORMAL = '\033[0m'

def circulo(raio):
    return math.pi * float(raio) ** 2


def help():
    print('É necessário informar o raio do circulo.')
    print(f'Sintaxe: python {sys.argv[0]} <valor do raio>')
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 
            'O raio deve ser um valor numerico',
            TerminalColor.NORMAL)  
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo: ', area)

'''
    Para Executar esse script, passar o valor no final
    python argumento_via_terminal 12.4
'''