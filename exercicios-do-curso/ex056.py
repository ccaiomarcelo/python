# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome 
# do homem mais velho e quantas mulheres têm menos de 20 anos.


from statistics import mean

nomes = []
idades = []
sexos = []
cont = 0
for i in range (0, 4):
    print(f'----- {i+1}ª PESSOA -----')
    nome = input('Nome: ')
    nomes.append(nome)
    idade = int(input('Idade: '))
    idades.append(idade)
    sexo = input('Sexo (M/F): ').upper()
    sexos.append(sexo)
    if sexo == 'F' and idade < 20:
        cont += 1

media = mean(idades)
if sexos[0] and sexos[1] and sexos[2] and sexos[3] == 'M':
    maior_idade = max(idades)
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')
    print('Não existem mulheres, sendo assim, não dá para dizer quantas tem menos de 20 anos!')

elif sexos[0] == 'M' and sexos[1] == 'M' and sexos[2] == 'M' and sexos[3] == 'F':
    maior_idade = max(idades[0], idades[1], idades[2])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'M' and sexos[1] == 'M' and sexos[2] == 'F' and sexos[3] == 'M':
    maior_idade = max(idades[0], idades[1], idades[3])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'M' and sexos[1] == 'M' and sexos[2] == 'F' and sexos[3] == 'F':
    maior_idade = max(idades[0], idades[1])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'M' and sexos[1] == 'F' and sexos[2] == 'M' and sexos[3] == 'M':
    maior_idade = max(idades[0], idades[2], idades[3])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'M' and sexos[1] == 'F' and sexos[2] == 'M' and sexos[3] == 'F':
    maior_idade = max(idades[0], idades[2])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'M' and sexos[1] == 'F' and sexos[2] == 'F' and sexos[3] == 'M':
    maior_idade = idades[0]
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'F' and sexos[1] == 'M' and sexos[2] == 'M' and sexos[3] == 'M':
    maior_idade = max(idades[1], idades[2], idades[3])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'F' and sexos[1] == 'M' and sexos[2] == 'M' and sexos[3] == 'F':
    maior_idade = max(idades[1], idades[2])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'F' and sexos[1] == 'M' and sexos[2] == 'F' and sexos[3] == 'M':
    maior_idade = max(idades[1], idades[3])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'F' and sexos[1] == 'M' and sexos[2] == 'F' and sexos[3] == 'F':
    maior_idade = idades[1]
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'F' and sexos[1] == 'F' and sexos[2] == 'M' and sexos[3] == 'M':
    maior_idade = max(idades[2], idades[3])
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'F' and sexos[1] == 'F' and sexos[2] == 'M' and sexos[3] == 'F':
    maior_idade = idades[2]
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'F' and sexos[1] == 'F' and sexos[2] == 'F' and sexos[3] == 'M':
    maior_idade = idades[3]
    pos_idade = idades.index(maior_idade)
    mais_velho = nomes[pos_idade]
    print(f'O homem mais velho é o {mais_velho}')

elif sexos[0] == 'F' and sexos[1] == 'F' and sexos[2] == 'F' and sexos[3] == 'F':
    print(f'Todas são mulheres, sendo assim, não é possivel dizer qual é o homem mais velho.')

print(f'A média de idade do grupo é de {media} anos.')
print(f'{cont} mulheres tem menos do que 20 anos.')
