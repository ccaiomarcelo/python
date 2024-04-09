# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual 
# foi o maior e o menor valores lidos. O programa deve perguntar ao usuário 
# se ele quer ou não continuar a digitar valores.

from statistics import mean
continuar = "S"
maior = []
cont = 0
while continuar == "S":
    n = int(input("Digite um número: "))
    maior.append(n)
    continuar = input("Quer continuar? [S/N]: ").upper().strip()[0]
print(f"Você digitou {len(maior)} números e a média foi de {mean(maior)}")
print(f"O maior valor foi {max(maior)} e o menor foi {min(maior)}")