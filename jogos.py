import forca
import adivinhacao

def escolha_jogo():
    print("********************************")
    print("******escolha o seu jogo********")
    print("********************************")

    print("---(1) Forca (2) Adivinhaçao---")

    jogo = int(input("Escolha um jogo?"))

    if (jogo == 1):
        print("Jogando forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhaçao")
        adivinhacao.jogar()
           


if(__name__ == "__main__"):
    escolha_jogo()