import valor

escolha = input('Deseja transformar Celsius ou Fahrenheit? 1 ou 2: ')
escolha = int(escolha)
print(escolha)


def verificarescolha(escolha, valor):
    if escolha == 1:
        valor = input('Digite o valor em C')
        valor = int(valor)
    else:
        return 'Fahrenheit'
    return valor


print(verificarescolha(escolha,valor))

# valor = input('Digite o valor (C): ')
# valor = int(valor)
# valortransformado = (valor * 9 / 5 + 32)
# print(valortransformado)


# valor = input('Digite o valor (F): ')
# valor = int(valor)
# valortransformado = ((valor - 32) * 5 / 9)
# print(valortransformado)
