'''
Criar uma função que vai jogar um dado de 6 numeros (sortear os numeros de 1 - 6)
criar um for que vai percorrer de 1 - 6
Se for impar continue
se o numero for par e igual ao valor sorteado pela função dado imprimir a string 'acertou' e depois chamar o break
Se não acertar chama o else (print numero errado)

'''
from random import randint

def sortear_dado():
    return randint(1, 6)

for i in range(1, 7):
    if i % 2 == 1:
        continue
    elif sortear_dado() == i:
        print("acertou mizeravi!!!", i)
        break
else:
    print("Errrrrooooooo")
