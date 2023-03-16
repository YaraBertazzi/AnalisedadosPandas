"""
Resumos e um pouco de Visualização no pandas
Resumo
Vamos ver alguns métodos para analisar nossas tabelas (dataframes)

Além disso, vamos usar os plot de gráfico padrões do pandas, mas no projeto de DataScience veremos outras mais bonitas e também muito práticas.

OBS: O pandas usa o matplotlib (que vimos na seção de "módulos e bibliotecas") para plotar gráficos.
Se quiser personalizar mais do que o padrão do pandas, importe o matplotlib e use os métodos do matplotlib
"""

import pandas as pd
import matplotlib

# Tratamento do DF
vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';') #sep é ondepassamos o parametro separador dp arquivo , encoding='ISO-8859-1'
produtos_df = pd.read_csv('Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv('Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv('Contoso - Clientes.csv', sep=';')

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
#print(vendas_df)
"""
 1 - Qual cliente que comprou mais vezes?
Usaremos o método .value_counts() para contar quantas vezes cada valor do Dataframe aparece
Usaremos o método .plot() para exibir um gráfico
"""

frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
print(frequencia_clientes)

frequencia_clientes[:5].plot()


"""
  2 - Qual a Loja que mais vendeu?
Usaremos o .groupby para agrupar o nosso dataframe, de acordo com o que queremos (somando as quantidades de vendas, por exemplo)
"""


"""
 Qual produto que menos vendeu?
Já temos uma lista criada para isso, basta verificarmos o final da lista (já que ela está ordenada) ou então usarmos os métodos:
min()
idxmin()
"""