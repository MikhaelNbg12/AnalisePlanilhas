import pandas as pd
from twilio.rest import Client

account_sid = 'AC6cb3794032ee12d01340e772eb181a78'
auth_token = 'cc39658e41d1a046e2f5934907cfb123'
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f' No mês {mes} alguém bateu a meta.Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            from_ ='+16365946177',
            body = f' No mês {mes} alguém bateu a meta.Vendedor: {vendedor}, Vendas: {vendas}',
            to = '+5513991038324')
        print(message.sid)