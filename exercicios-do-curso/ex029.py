# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado.
# A multa vai custar 7 reais por cada Km/h acima do limite.

velocidade = int(input('Digite a velocidade do seu carro em km/h '))
if velocidade > 80:
    diferença = velocidade - 80
    print(f'Multa aplicada. Valor: R$ {(velocidade - 80)*7}')
    print(f'Você passou a {diferença} km/h além do limite de 80 km/h.')
