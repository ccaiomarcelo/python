# Desenvolva um programa que leia seis números inteiros e mostre a soma 
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
pares = []
for i in range(1, 7):
    num = int(input('Numero inteiro para somar: '))
    if num % 2 == 0:
        pares.append(num)
        soma += num
print(f'Números pares digitados: {pares}')
print(f'Soma dos números pares: {soma}')