# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso 
# de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Pode ser formado um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Pode ser formado um triângulo ISÓSCELES.')
    else:
        print('Pode ser formado um triângulo ESCALENO.')
else:
    print(f'{r1}, {r2} e {r3} não podem formar um triângulo.')