# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome 
# do homem mais velho e quantas mulheres têm menos de 20 anos.


from statistics import mean

nomes = []
idades = []
sexos = []
for i in range (1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = [input('Nome: ')]
    nomes.append(nome)
    idade = [int(input('Idade: '))]
    idades.append(idade)
    sexo = [input('Sexo (M/F): ').upper()]
    sexos.append(sexo)

media = mean(idades)
if sexo[0] and sexo [1] and sexo[2] and sexo[3] == 'M':
    midade = max(idades)
    posidad = idades.find(midade)
    maisvelho = nomes[posidad]
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho é o {maisvelho}')