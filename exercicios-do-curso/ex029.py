# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado.
# A multa vai custar 7 reais por cada Km/h acima do limite.

from colorama import Fore, init, Style
init()

cor = {
    'ciano': Fore.LIGHTCYAN_EX,
    'vermelho': Fore.RED,
    'amarelo': Fore.YELLOW,
    'reset': Fore.RESET,
}

estilo = {
    'negrito': Style.BRIGHT,
    'reset': Style.RESET_ALL
}

velocidade = int(input(f"{cor['ciano']} Digite a velocidade do seu carro em {cor['reset']}{cor['amarelo']}km/h {cor['reset']}"))
if velocidade > 80:
    diferença = velocidade - 80
    print(f"{cor['vermelho'] + estilo['negrito']}{'Multa'.upper()} aplicada.{estilo['reset']} Valor: {cor['vermelho'] + estilo['negrito']}R$ {(velocidade - 80)*7} {estilo['reset']}")
    print(f"Você passou a{cor['vermelho']}{estilo['negrito']} {diferença} km/h{estilo['reset']} além do limite de {cor['vermelho'] + estilo['negrito']}80 km/h. {estilo['reset']}")
