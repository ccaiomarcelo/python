saque = int(input('Quanto quer sacar: R$ '))

rest100 = saque % 100

int50 = rest100 // 50
rest50 = rest100 % 50

int20 = rest50 // 20
rest20 = rest50 % 20

int10 = rest20 // 10
rest10 = rest20 % 10

int5 = rest10 // 5
rest5 = rest10 % 5

int2 = rest5 // 2
rest2 = rest5 % 2

print(f'{saque//100} Nota(s) de 100.')
print(f'{int50} Nota(s) de 50.')
print(f'{int20} Nota(s) de 20.')
print(f'{int10} Nota(s) de 10.')
print(f'{int5} Nota(s) de 5.')
print(f'{int2} Nota(s) de 2.')

