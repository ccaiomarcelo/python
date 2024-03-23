# Refaça o DESAFIO 9, mostrando a tabuada de um número que o 
# usuário escolher, só que agora utilizando um laço for.

print('-=' * 4)
print('TABUADA')
print('-=' * 4)

num = int(input('Quer saber a tabuada de qual número? '))
mult = int(input('Quer multiplicar até quanto? '))

for i in range(0, mult+1):
    print(f'{num} x {i:2} = {num*i}')
print('FIM.')