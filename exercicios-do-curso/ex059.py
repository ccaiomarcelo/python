# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

import os

opção = 0
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
while opção != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Saber o maior\n[4] Digitar novos números\n[5] Sair do programa')
    opção = int(input('Sua opção: '))
    if opção == 1:
        print('-=' * 10)
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
        print('-=' * 10)
    elif opção == 2:
        print('-=' * 10)
        print(f'A multiplicação entre {n1} x {n2} é {n1*n2}')
        print('-=' * 10)
    elif opção == 3:
        print('-=' * 10)
        print(f'Maior valor entre {n1} e {n2} é {max(n1, n2)}')
        print('-=' * 10)
    elif opção == 4:
        os.system('clear')
        print('------ Informe os números novamente ------')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
print('Programa encerrado.')