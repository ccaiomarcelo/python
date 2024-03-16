# Programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex: DIgite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

num = int(input('Digite um número entre 0 e 9999: '))
a = num // 1 % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10

print(f'Unidade: {a}')
print(f'Dezena: {b}')
print(f'Centena: {c}')
print(f'MIlhar: {d}')