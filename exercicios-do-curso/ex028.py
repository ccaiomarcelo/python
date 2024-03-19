# Escreva um programa que faça o computador "pensar" em um número intero entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

import random 
import time
print('-=-' * 25)
print('Pensei em um número entre 0 e 5. Você consegue adivinhar em qual pensei?')
print('-=-' * 25)
numero = random.randint(0, 5)
numusu = int(input('Digite qual você acha: '))
print('VERIFICANDO...')
time.sleep(2)
if numero == numusu:
    print(f'Você acertou! Número do computador: {numero}')
else:
    print(f'Você ERROU! Número do computador: {numero}')