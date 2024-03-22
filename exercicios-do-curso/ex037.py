# Exercício Python 37: Escreva um programa em Python que 
# leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão:')
print('[1] - converter para BINÁRIO')
print('[2] - converter para OCTAL')
print('[3] - converter para HEXADECIMAL')
print('[4] - converter para todos acima')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero) [2:]}')
elif opção == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero) [2:]}')
elif opção == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero) [2:]}')
elif opção == 4:
    print(f'''{numero} em BINÁRIO: {bin(numero) [2:]}
{numero} em OCTAL: {oct(numero) [2:]}
{numero} em HEXADECIMAL {hex(numero) [2:]}''')
else:
    print('Opção inválida. Por favor, digite uma opção válida.')

