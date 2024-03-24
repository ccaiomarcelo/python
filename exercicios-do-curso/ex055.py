# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
lista = []
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    lista.append(peso)
print(f'{max(lista)} foi o maior peso e {min(lista)} foi o menor peso.')