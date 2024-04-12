idade = input('Qual a sua idade? ')
idade = int(idade)


def verificaidade(idade):
    if (idade >= 18) and (idade <= 65):
        verificacao = 'pode votar'
    else:
        verificacao = 'não pode votar'
    return verificacao


print(idade)
verificacao = verificaidade(idade)
print(f'Sua idade é {idade} e você {verificacao}')
