# Crie um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'{numero} é PAR!')
else:
    print(f'{numero} é IMPAR!')