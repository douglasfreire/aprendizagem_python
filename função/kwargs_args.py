'''
Não é necessário escrever *args ou **kwargs. 
Somente o *(astérisco) é necessário. 
Você também poderia ter escrito *var e **vars. 
Escrever *args e **kwargs é apenas uma convenção.

*args é usado para enviar uma lista de argumentos sem palavra-chave para a função.
Irá gerar uma tupla.

**kwargs permite que você passe um argumento nomeado como palavra-chave para uma função. 
Irá gerar um dicionário.


'''
# Função normal
def soma(a, b):
    return a + b

# Função usando *args
def soma_n(*numeros):
    soma = 0 
    for n in numeros:
        soma += n
    return soma

# Função usando **Kwargs
def soma_kwargs(**valores):
    soma = 0
    for key, value in valores.items():
        soma += value
    return soma

if __name__ == "__main__":
    # print(soma(2, 3))
    # print(soma_n(1, 2))
    # print(soma_n(1, 1, 1, 1, 1, 1))
    print(soma_kwargs(A = 2, B = 3))
    print(soma_kwargs(A = 2, B = 3, C = 4, D = 5))