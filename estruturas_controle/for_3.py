produto = {'nome': 'Caneta Chic', 'preco': 14.99, 
            'importada': True, 'estoque': 793}

for key in produto:
    print(key)
print('#########################################')
for value in produto.values():
    print(value)
print('#########################################')
for  key, value in produto.items():
    print("".join([key, ' = ', str(value)]))