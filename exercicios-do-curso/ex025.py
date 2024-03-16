# Crie um programa que leia o nome de uma pessoa e veja se ela tem Silva no nome

nome = input('Digite o seu nome completo: ').strip()
print(f"O seu nome possui Silva?: {'SILVA' in nome.upper()}")