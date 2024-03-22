# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nome = input('Qual o seu nome? ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A sua média foi de: {media}')
if media < 5:
    print(f'Aluno {nome} REPROVADO.')
elif media >= 5 and media <= 6.9:
    print(f'Aluno {nome} de RECUPERAÇÃO.')
elif media >= 7:
    print(f'Aluno {nome} APROVADO.')
