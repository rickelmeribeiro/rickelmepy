import random


def jogo_adivinhacao():
    while True:
        numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
        tentativas = 0

        print("Bem-vindo ao jogo de adivinhação!")
        print("Estou pensando em um número entre 1 e 100.")

        while True:
            try:
                tentativa = int(input("Tente adivinhar o número: "))
                if tentativa <= 0 or tentativa > 100:
                    print("Por favor, insira um número entre 1 e 100.")
                    continue

                tentativas += 1

                if tentativa < numero_secreto:
                    print("Tente um número maior.")
                elif tentativa > numero_secreto:
                    print("Tente um número menor.")
                else:
                    print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                    break
            except ValueError:
                print("Por favor, insira apenas números inteiros.")


if __name__ == "__main__":
    jogo_adivinhacao()
