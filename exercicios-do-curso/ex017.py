from math import hypot

CatOp = float(input('Digite o Cateto Oposto: '))
CatAd = float(input('Digita o Cateto Adjacente: '))

hip = hypot(CatOp, CatAd)

print(f'Hipotenusa: {hip:.2f}')