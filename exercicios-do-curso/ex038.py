# Escreva um programa que leia dois números inteiros e compare-os 
# mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

if numero1 > numero2:
    print('O PRIMEIRO é maior.')
elif numero1 < numero2:
    print('O SEGUNDO é maior')
else:
    print('Os número são iguais.')