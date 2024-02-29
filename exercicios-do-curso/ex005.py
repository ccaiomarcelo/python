a = int(input('Digite um número: '))
print(f'Sucessor {a+1} e antecessor {a-1}')
print(f'Dobro {a*2}, triplo {a*3} e raíz quadrada {a**(1/2):.3f}')

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
print(f'Média: {(n1+n2)/2:-^10}')

print('\n ----- Agora vamos converter um número em CM e MM-----')
cmmm = float(input('Digite um número em metros: '))
print(f'Em cm {cmmm*100:-^10}, em mm {cmmm*1000:-^10}')

print('\n ----- Calcular tabuada de um número até 5 -----')
num = int(input('Número: '))
print(f'{num}x1 = {num*1}')
print(f'{num}x2 = {num*2}')
print(f'{num}x3 = {num*3}')
print(f'{num}x4 = {num*4}')
print(f'{num}x5 = {num*5}')

print('\n ----- Conversão de R$ para $ -----')
conv = float(input('Digite o valor em reais R$ '))
print(f'Você pode comprar {conv/4.933:.2f} dólares.')