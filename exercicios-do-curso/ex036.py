# Crie um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em quantos
# anos ele quer pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
# do salário ou então o empréstimo será negado.

print('===-==='*7)
print('CÁLCULO DE EMPRÉSTIMO BANCÁRIO -> COMPRA DE IMÓVEL')
print('===-==='*7)

salario = float(input('\nPrimeiro, informe o seu salário atual: R$ '))
valcasa = float(input('Qual o valor da casa para financiar? R$ '))
temppag = int(input('Em quantos anos você quer pagar? '))
prestmens = valcasa / (temppag*12)

if prestmens > salario*0.30:
    print('\nEmpréstimo NEGADO. O valor da prestação excede 30% do seu salário.')
    print(f'\nValor da prestação: {prestmens:.2f}')
    print(f'Valor de 30% do seu salário: R$ {salario*0.30:.2f}')
else:
    print('\nSeu empréstimo foi APROVADO!')
    print(f'\nValor total do empréstimo: R$ {valcasa}')
    print(f'Quantidade de parcelas: {temppag*12}')
    print(f'Valor da parcela: R$ {prestmens:.2f}')