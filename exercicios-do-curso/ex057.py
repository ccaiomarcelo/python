# Faça um programa que leia o sexo de uma pessoa, mas só aceite 
# os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite o seu sexo (M ou F): ').upper().strip()
while 'F' != sexo != 'M':
    sexo = input('Dados inválidos. Por favor, informe o seu sexo: ').strip().upper()
print(f'Sexo {sexo} guardado com sucesso.')

