# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Termo: '))
razão = int(input('Razão: '))
cont = 1
while not cont == 11:
    print(termo, end=' > ')
    termo += razão
    cont += 1
print('FIM.')