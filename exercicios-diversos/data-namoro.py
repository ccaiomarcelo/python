from datetime import *

data_pedido_namoro = datetime(2023, 10, 29)
data_hoje = datetime.today()

diferença = data_hoje - data_pedido_namoro

print('========== Tempo de namoro. ==========')
print(f'{diferença.days} dias.')
print(f'{diferença.days / 30:.0f} meses.')

