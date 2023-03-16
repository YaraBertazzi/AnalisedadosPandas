from typing import Any

import pandas as pd
from pandas import DataFrame

vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';') #sep é ondepassamos o parametro separador dp arquivo , encoding='ISO-8859-1'
produtos_df = pd.read_csv('Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv('Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv('Contoso - Clientes.csv', sep=';')

"""print(vendas_df)
print(produtos_df)
print(lojas_df)
print(clientes_df)"""

# retirar colunas: clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9','Unnamed: 10'], axis=1) #axis 1 eixo de coluna , axis=2 eixo de linha

#para pegar só as colunas que ira usar
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

print(vendas_df)
print(produtos_df)
print(lojas_df)
print(clientes_df)

# Juntar DataFrame / mesclar
# o merge precisa de duas colunas com o mesmo nome
#vai pegar tabela produtos com a coluna ID Produto como referencia, a coluna ID Produto tem na tabela venda e produto

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

print(vendas_df)

# renomear o nome da coluna (pasa o nome da coluna que ser amodificada o nome , dentro dos parente de rename em dicionario [nome antigo: nome novo])
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
print(vendas_df)