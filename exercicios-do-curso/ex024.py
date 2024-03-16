cidade = input('Qual a cidade que você mora: ').strip()
print(f"Sua cidade começa com Santo?: {cidade[:5].upper() == 'SANTO'}")
