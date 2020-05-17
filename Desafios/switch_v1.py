'''
Criar uma função que retorne se 
é dia de semana 
ou fim de semana
'''

def get_semana_dia(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado'
    }

    return dias.get(dia)

if __name__ == "__main__":
    for dia in range(1, 8):
        if dia == 1 or dia == 7:
            print("".join(['Dia: ', get_semana_dia(dia), ', status: fim de semana']))
            
        else:
            print("".join(['Dia: ', get_semana_dia(dia), ', status: Dia util']))