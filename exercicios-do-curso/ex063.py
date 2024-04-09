# Escreva um programa que leia um número N inteiro qualquer e 
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci
# Sequência de números inteiros, começando normalmente por 0 e 1, 
# na qual cada termo subsequente corresponde à soma dos dois anteriores: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-'*20)
print("Sequência de Fibonacci")
print('-'*20)
numero = int(input('Quantos termos você quer mostrar?: '))
cont = 0

termoant = 0
fibonacci = 1

while cont < numero:
    print(termoant, end=" > ")
    proximo = termoant + fibonacci
    termoant = fibonacci
    fibonacci = proximo
    cont += 1
print("FIM")