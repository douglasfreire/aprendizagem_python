tabuada_2 = {i: i * 2 for i in range(11)}
# print(tabuada_2)

print("### Tabuada de 2 ###")
for numero, resultado in tabuada_2.items():
    print(f'{numero} x 2 = {resultado}')

dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
# print(dicionario)

print("### Valores dobro """)
for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')