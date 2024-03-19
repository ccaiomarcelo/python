# Escreva um programa que leia o salário de um funcionário e calcule o valor
# do seu aumento. Para salários superiores a 1250 reais, aumente 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário: ')) 
if salario > 1250:
    print(f'Seu salário com aumento de 10%: R$ {salario*1.10:.2f}')
else:
    print(f'Seu salário com aumento de 15%: R$ {salario*1.15:.2f}')