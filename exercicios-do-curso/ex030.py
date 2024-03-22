# Crie um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

from colorama import Fore, init, Style
init()

estilo = {
    'negrito': Style.BRIGHT,
    'reset': Style.RESET_ALL
}

cor = {
    'azul-claro': Fore.LIGHTBLUE_EX,
    'verde-claro': Fore.LIGHTGREEN_EX,
    'amarelo-claro': Fore.LIGHTYELLOW_EX,
    'reset': Fore.RESET
}

numero = int(input(f"{cor['azul-claro']}Digite um número: {cor['reset']}"))
if numero % 2 == 0:
    print(f"{cor['verde-claro']}{numero} {cor['reset']}é {cor['verde-claro'] + estilo['negrito']}PAR! {estilo['reset']}")
else:
    print(f"{cor['amarelo-claro']}{numero} {cor['reset']}é {cor['amarelo-claro'] + estilo['negrito']}IMPAR!")