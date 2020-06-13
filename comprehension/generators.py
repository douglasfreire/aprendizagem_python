'''
O generator consome menos memoria,  do que a list comprehension que gera a lista completa
O generator vai gerando os dados sob demanda
'''


generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) # Aqui geraa um erro
