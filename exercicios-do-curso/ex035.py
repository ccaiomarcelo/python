# Desenvolva um programa que leia o comprimento de 3 retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if a< b + c and b < a + c and c < a + b:
    print(f'{a}, {b} e {c} podem formar um triângulo.')
else:
    print(f'{a}, {b} e {c} não podem formar um triângulo.')