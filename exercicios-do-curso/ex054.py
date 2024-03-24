# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0
anoatual = date.today().year
for i in range(1, 8):
    ano = int(input(f'Ano de nascimento da {i}ª pessoa: '))
    if anoatual - ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'No total {maior} pessoas são maiores de idade e {menor} são menores.')
