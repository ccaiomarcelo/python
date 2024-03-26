# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
# em um número entre 0 e 10. Só que agora o jogador vai tentar 
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

cont = 0
print('Pensei em um número de 0 a 10. Você consegue adivinhar qual?')
computador = randint(0, 10)
print(computador)
jogador = int(input('Sua tentativa: '))
while jogador != computador:
    print('Você errou! Tente novamente.')
    if jogador < computador:
        print('Mais pra cima...')
    else:
        print('Mais pra baixo...')
    jogador = int(input('Sua opção: '))
    cont += 1
print(f'Você acertou! Tentativas: {cont}')
print(f'Número do computador {computador}')