# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

import datetime
ano = int(input('Digite um ano para descobrir se ele é bissexto (digite 0 para colocar o ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')