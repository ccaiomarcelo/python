# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = soma = contador = 0
cont = int(input("Digite um número [999 para parar]: "))
while cont != 999:
    soma += cont
    contador += 1
    cont = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {contador} números e a soma entre eles foi {soma}")