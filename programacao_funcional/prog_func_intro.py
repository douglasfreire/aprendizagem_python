

def executar(funcao):
    if callable(funcao):
        funcao()
    else:
        print('Argumento na função não pode ser chamado')


def bomdia():
    print('Bom dia')


def boatarde():
    print('boa tarde')


if __name__ == "__main__":
    executar(bomdia)
    executar(boatarde)
    executar(1)