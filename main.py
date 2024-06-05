import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maiore', 'junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

print(tabela_vendas)