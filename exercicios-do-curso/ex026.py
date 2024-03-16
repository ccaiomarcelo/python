# Ler uma frase qualquer e mostre
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase: ').upper().strip()
print(f"""Tem {frase.count('A')} letras A""")
print(f"""Primeira posição do A: {frase.find('A')}""")
print(f"""Última posição do A: {frase.rfind('A')}""")
