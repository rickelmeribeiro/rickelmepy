nome = input('Qual seu nome?')
sobrenome = input('Qual seu sobrenome?')
idade = input('Qual sua idade?')
idade = int(idade)


def verificaridade(idade):
    if idade < 18:
        verificacao = 'Menor de idade'
    else:
        verificacao = 'Maior de idade'
    return verificacao


print(nome)
print(sobrenome)
print(idade)
verificacao = verificaridade(idade)
print(f'Olá {nome}{sobrenome}, {verificacao}')
