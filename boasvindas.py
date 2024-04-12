nome = input('Qual seu nome?')
horas = input('Quantas horas?')
horas = int(horas)


def verificarhora(horas):
    if (horas >= 6) and (horas <= 11):
        temp = 'Bom dia'
    elif (horas >= 12) and (horas <= 17):
        temp = 'Boa Tarde'
    else:
        temp = 'Boa Noite'
    return temp

print(nome)
print(horas)
horario = verificarhora(horas)
print(f'Olá Sr. {nome}, {horario}')