# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM
import random
print("você consegue acerta o número que o robor escolheu?")
com = random.randint(0,5)
seun= int(input("Digite números entre 0 e 5:"))
if com == seun:
    print("você venceu!!!")

else:
    print("você perdeu!!!")
    print(f"o robo escolheu o número {com}")

