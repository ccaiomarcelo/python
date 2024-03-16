nome = input('Digite o teu nome completo: ')

print(f'Caracteres: {len(nome)}')
print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
rep = nome.replace(' ', '')
print(f'Caracteres sem espaço: {len(rep)}')
primnome = nome.split()
print(f'Primeiro nome: {len(primnome[0])}')

print(f'Quantidade de caracteres do segundo nome: {len(primnome[1])}')