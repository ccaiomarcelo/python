# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

ppt = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(ppt)
print('Suas opções: ')
print('''
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
''')
opção = int(input('Qual é a sua jogada? '))
if opção == 1:
    jogador = 'PEDRA'
elif opção == 2:
    jogador = 'PAPEL'
elif opção == 3:
    jogador = 'TESOURA'
else:
    print('Opção inválida. Tente novamente.')
    exit()
    
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=-' * 15)
print(f'Computador jogou {computador}')
print(f'Jogador jogou {jogador}')
print('-=-' * 15)

if jogador == computador:
    print('EMPATOU!')
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print('JOGADOR VENCE')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('COMPUTADOR VENCE')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('JOGADOR VENCE')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('COMPUTADOR VENCE')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('COMPUTADOR VENCE')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('JOGADOR VENCE')