import random
import carregar_palavra

def inicializa_letras_acertadas():
    lista = ["_" for letras in palavra_secreta]
    return lista

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def jogar():

    mensagem_abertura()
    palavra_secreta = carregar_palavra()

    print("a palavra secretá é:")
    print(letras_certas)
    print("")

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input("informe uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_certas[index]=letra
                index += 1        
        else:
            erros += 1
        enforcou = erros == 6 
        acertou = "_" not in letras_certas
        print(letras_certas)

    if(acertou):
        print("você ganhou!")
    else:
        print("você perdeu")


if(__name__ == "__main__"):
    jogar()
