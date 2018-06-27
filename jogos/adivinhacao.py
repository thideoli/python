import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

dificuldade = 0
print("\n")
print("(1) Fácil - (2) Médio - (3) Difícil - (q) Sair")
while(dificuldade != "1" and dificuldade != "2" and dificuldade != "3"):
    dificuldade = input("Informe a dificuldade desejada: ")
    if(dificuldade == "q"):
        break

if(dificuldade != "q"):
    dificuldade = int(dificuldade)

    if(dificuldade == 1):
        numero_maximo = 26
    elif (dificuldade == 2):
        numero_maximo = 51
    elif (dificuldade == 3):
        numero_maximo = 101

    numero = random.randrange(1, numero_maximo)

    tentativas = 0

if(dificuldade != "q"):
    nao_acertou = True
else:
    print("Você saiu!")
    nao_acertou = False

while(nao_acertou):
    tentativas = tentativas + 1

    print("\n")
    chute = input("Chute um número de 1 até {} ou pressione \"q\" para sair: ".format(numero_maximo - 1))
    if(chute == "q"):
        print("Você saiu!")
        break

    try:
        chute = int(chute)
    except:
        continue

    print("Você chutou o número {} na tentativa {}".format(chute, tentativas))

    if(chute > numero):
        print("Você errou, tente um número menor!")
    elif(chute < numero):
        print("Você errou, tente um número maior!")
    else:
        print("Você acertou!")
        nao_acertou = False

print("\n")
print("************")
print("Fim do jogo!")
print("************")