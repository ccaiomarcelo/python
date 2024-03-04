import random

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

sorteio = [(a1), (a2), (a3), (a4)]

print(f'Aluno escolhido: {random.sample(sorteio, 4)}')