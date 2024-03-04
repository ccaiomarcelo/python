CatOp = float(input('Digite o Cateto Oposto: '))
CatAd = float(input('Digita o Cateto Adjacente: '))

hip = (CatOp*CatOp) + (CatAd*CatAd)

print(f'A hipotenusa ao quadrado é: {hip}\nA hipotenusa é: {hip**1/2}')