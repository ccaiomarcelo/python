# Elabore um programa que calcule o valor a ser 
# pago por um produto, considerando o seu preço 
# normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Valor da compra: R$ '))
print('''Qual a forma de pagamento?\n
[1] à vista no dinheiro ou cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
forma = int(input('Sua opção: '))

if forma == 1:
    print(f'\nVocê pagará R$ {valor - (valor*0.10):.2f} ao invés de R$ {valor:.2f}')
elif forma == 2:
    print(f'\nVocê pagará R$ {valor - (valor*0.05):.2f} ao invés de R$ {valor}')
elif forma == 3:
    print(f'\nVocê pagará em 2x de R$ {valor/2:.2f} sem juros.')
elif forma == 4:
    parcelas = int(input('Quer parcelar em quantas vezes? '))
    print(f'O valor ficou parcelado em {parcelas}x de R$ {(valor * 1.20) / parcelas:.2f} com JUROS.')
    print(f'Sua compra de R$ {valor} custará R$ {valor * 1.20:.2f}')
else:
    print('Digite uma opção válida. Tente novamente.')