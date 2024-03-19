n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n3 = float(input('Digite a sua terceira nota: '))
medgeral = int(input('Qual é a média da sua escola/faculdade? '))
media = (n1 + n2 + n3) / 3

if media <= medgeral:
    print(f'Aluno REPROVADO com média {media:.2f}')
else:
    print(f'Aluno APROVADO com média {media:.2f}')
print('----------FIM----------')