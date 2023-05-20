import random

def jogar():
    print()
    print("********************************")
    print("bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print(" ")
    print("Selecione o nivel de dificuldade!")
    print("(1) Fácil (2) Médio (3) Difícil")
    print(" ")

    nivel = int(input("Defina o nivel!"))
    print(" ")
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativas {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        print(" ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou o numero secreto!!!")
            print(f"E ficou com {pontos} !!! ")
            break
        else:
            if maior:
                print()
                print("Você errou!!! seu numero foi maior que o numero secreto!!!")
                print()
            elif menor:
                print()
                print("Você errou!!! seu numero foi menor que o numero secreto!!!")
                print()
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos


    print(" ")
    print(f"O numero secreto era: {numero_secreto} !!!")
    print(" ")
    print("**********************************")
    print("Fim do Jogo")
    print("**********************************")
    sair = input("escreva qualquer coisa para sair!!!")  


if(__name__ == "__main__"):
    jogar()