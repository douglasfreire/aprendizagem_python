'''
Dessa forma ele executará o else normalmente
'''
for i in range(1, 10):
    print(i)
else:
    print('Finished')

print('##########################################')
'''
Quando ele encontra um break, o 'else' não será executado
'''
for i in range(1, 10):
    if i == 6:
        break
    print(i)
else:
    print('Finished')