'''
Aqui o for será usado para percorrer uma string, lista, tupla e set
'''

palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=',')
print()
print()
aprovados = ['Douglas', 'Ully', 'Camila', 'Tomedi', 'Danilo']
for nome in aprovados:
    print(nome)

print('##########################################')
print()

for posicao, nome in enumerate(aprovados):
    print(f'{posicao +1})', nome)


print('##########################################')
print()

dias_semana = ('Domingo', 'Segunda', 'Terça', 
                'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia in dias_semana:
    print(f'Hoje é {dia}')

print('##########################################')
print()

for letra in set('Muito legal'):
    print(letra)