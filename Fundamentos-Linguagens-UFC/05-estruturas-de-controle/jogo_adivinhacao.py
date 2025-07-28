import random

print("🔢 Bem-vindo ao Jogo da Adivinhação!")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        chute = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1

        if chute < numero_secreto:
            print("Tente um número maior.")
        elif chute > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
    except ValueError:
        print("Por favor, digite um número válido.")
