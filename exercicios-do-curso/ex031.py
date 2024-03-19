# Digite um programa que leia a distância de uma viagem em km
# Calcule o preço da passagem do ônibus cobrando 0,50 reais
# por km para viagem de até 200 km e 0.45 reais para viagens mais longas.

distancia = int(input('Digite a distância da viagem em km: '))
print('Lembrando que até 200 km, cobramos R$ 0,50 por km e R$ 0,45 para mais longas.')

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print(f'O valor da passagem ficou: R$ {passagem} para {distancia} km')