nome = input('Qual o teu nome? ')
print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print(f'A soma é: {n1+n2}', end=' ')
print(f'A subtração é: {n1-n2}')
print(f'O produto é {n1*n2} \n e a divisão é {n1/n2:.3f}')
print(f'Divisão inteira {n1//n2}, resto {n1%n2} e potência {n1**n2}')