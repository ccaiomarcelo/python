# Escreva um programa que faça o computador "pensar" em um número intero entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

from colorama import Fore, init
from random import randint 
from time import sleep

init()

color = {
    'yellow': Fore.YELLOW,
    'red': Fore.RED,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'green': Fore.GREEN,
    'reset':Fore.RESET,
}

division = (color['yellow'] + '-=-' + color['reset']) * 25

print(division)
print(f"{color['blue']} Pensei em um número entre 0 e 5. Você consegue adivinhar em qual pensei?")
print(division)
numero = randint(0, 5)
numusu = int(input(f"\n {color['blue']} Digite qual você acha: {color['reset']}"))
print(f"\n {color['magenta']} VERIFICANDO...{color['reset']}")
sleep(2)
if numero == numusu:
    print(f"\n {color['green']} Você acertou!{color['reset']} \n Número do computador: {numero}")
else:
    print(f"\n {color['red']} Você ERROU!{color['reset']} \n Número do computador: {numero}")