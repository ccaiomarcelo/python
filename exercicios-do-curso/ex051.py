# Desenvolva um programa que leia o primeiro termo e a razão 
# de uma PA. No final, mostre os 10 primeiros termos dessa progressão

print('=' * 10)
print('10 termos de uma PA')
print('=' * 10)

termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))

for i in range(1, 11):
    print(termo, end=' > ')
    termo += razão
print('ACABOU.')