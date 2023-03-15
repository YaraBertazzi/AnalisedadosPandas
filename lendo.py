import pandas as pd

vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';') #sep é ondepassamos o parametro separador dp arquivo

vendas_df.info()

#lista de clientes
lista_clientes = vendas_df['ID Cliente']
print(lista_clientes)

#lista de produtos e sua quantidade
produtos_quantidade = vendas_df[['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']]
print(produtos_quantidade)