# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome 
# do homem mais velho e quantas mulheres têm menos de 20 anos.

from statistics import mean
nomes = []
idades = []
cont = 0
for i in range (0, 4):
    print(f'----- {i+1}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()
    if sexo == 'F' and idade < 20:
        cont += 1
    if sexo == 'M':
        nomes.append(nome)
        idades.append(idade)
media = mean(idades)
max_idade = max(idades)
mais_velho = nomes[idades.index(max_idade)]
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {max_idade} e se chama {mais_velho}.')
print(f'Ao todo são {cont} mulheres com menos de 20 anos.')
