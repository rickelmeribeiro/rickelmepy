conversor = int(input("Digite 1 para C -> F ou Digite 2 para F -> C: "))
temperatura = float(input("Digite a temperatura: "))


def escolher(conversor, temperatura):
    if conversor == 1:
        return (temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9


print(escolher(conversor, temperatura))
