import os
from random import randint

os.system("cls")
print("Seja bem vindo ao Jokenpô")
print("Esse jogo exige que você escolha uma das opções abaixo")
print("Digite 1 - Para Opção Pedra")
print("Digite 2 - Para Opção Papel")
print("Digite 3 - Para Opção Tesoura")

opcaoEscolhida = input()

opcaoComputador = randint(1,3)

print("Escolha jogador foi ", opcaoEscolhida)
print("Escolha computador foi ", opcaoComputador)

opcaoEscolhida = int(opcaoEscolhida)

# Ganho
# 1 - 3; 2 - 1, 3 - 2 
if (opcaoEscolhida == 1 and opcaoComputador == 3) or (opcaoEscolhida == 2 and opcaoComputador == 1) or (opcaoEscolhida == 3 and opcaoComputador == 2) :
    print("Você ganhou")
#Perdeu
# 1 - 3; 2 - 1, 3 - 2 
elif (opcaoEscolhida == 3 and opcaoComputador == 1) or (opcaoEscolhida == 1 and opcaoComputador == 2) or (opcaoEscolhida == 2 and opcaoComputador == 3) :
    print("Você perdeu")
else:
    print("Você empatou")
