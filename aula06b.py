n = input('Digite algo: ')



print(f'É numérico? {n.isnumeric()}') 
print(f'É letra? {n.isalpha()}') 
print(f'É número e letra? {n.isalnum()}') 
print(f'Está tudo maiúsculo {n.isupper()}') 
print(f'Tem a primeira letra maiúscula e o resto minúsculo? {n.istitle()}')
print(f'É tudo minúsculo? {n.islower()}')