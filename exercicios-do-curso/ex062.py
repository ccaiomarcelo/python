# Melhore o DESAFIO 61, perguntando para o usuário se ele quer  
# mostrar mais alguns termos. O programa encerrará quando ele disser 
# que quer mostrar 0 termos.

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
opção = 1
contermos = 0
while not opção == 0:
    while not cont == 11:
        print(termo, end=' > ')
        termo += razão
        cont += 1
    print('PAUSA') 
    opção = int(input('Quantos termos quer mostrar a mais? '))
    contermos += opção
    cont2 = 1
    while not cont2 == opção + 1:
        print(termo, end=' > ')
        termo += razão
        cont2 += 1

print(f'Progressão finalizada com {(contermos + cont) - 1} termos mostrados.')

