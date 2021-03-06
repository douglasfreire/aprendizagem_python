'''
Para sinalizar uma constante no python, 
a variavel precisa ser escrita com letras maiusculas
'''

PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'politica'}

textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida',
    'Maria possui religião'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui pelo menos uma palavra probida: ', palavra)
            break
    
    else:
        print('Texto liberado: ', texto)