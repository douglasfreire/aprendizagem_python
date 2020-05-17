PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'politica'}

textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida',
    'Maria possui religião'
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavra proibida: ', intersecao)
    else:
        print('Texto autorizado: ', texto)