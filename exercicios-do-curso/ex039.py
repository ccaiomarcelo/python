# Faça um programa que leia o ano de nascimento 
# de um jovem e informe, de acordo com a sua idade, se ele ainda vai 
# se alistar ao serviço militar, se é a hora exata de se alistar ou 
# se já passou do tempo do alistamento. Seu programa também deverá
# mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('---------- CÁLCULO DE ALISTAMENTO ----------')
sexo = input('Qual o seu sexo? (M/F) ').upper()
if sexo == 'M':
    anonasc = int(input('Ano de nascimento: ')) 
    ano = date.today().year
    idade = ano - anonasc
    print(f"Quem nasceu em {anonasc} tem {idade} anos em {ano}")

    if idade > 18:
        print(f'Você deveria ter se alistado há {idade-18} anos.')
        print(f'Seu alistamento foi em {anonasc+18}')
    elif idade < 18:
        print(f'Ainda faltam {18-idade} anos para o seu alistamento.')
        print(f'Seu alistamento será em {anonasc+18}.')
    else:
        print('Você deve se alistar IMEDIATAMENTE!')
else:
    print('Você não precisa se alistar OBRIGATORIAMENTE.')