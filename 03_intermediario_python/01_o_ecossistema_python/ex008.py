"""Realização de cálculos com pandas
Agora, você recebeu um arquivo CSV chamado sales.csv que contém dados de vendas com três colunas: "user_id", "date", e "order_value".

Usando o pandas, você lerá o arquivo e calculará as estatísticas sobre os valores de vendas.

Da mesma forma que você pode acessar um dicionário pela sua chave, por exemplo, dictionary["key_name"], você pode usar a mesma sintaxe em pandas para acessar uma coluna! Além disso, o pacote também oferece métodos úteis para realizar cálculos em DataFrames ou subconjuntos de DataFrames (como colunas)!

Exemplos dessa sintaxe incluem df["column_name"].mean() e df["column_name"].sum() para calcular a média e o total de uma determinada coluna, respectivamente.

Leia "sales.csv", salvando como um DataFrame do pandas chamado sales_df.

Acesse a coluna "order_value" de sales_df e, em seguida, chame o método .mean() para encontrar o valor médio do pedido.

Acesse a coluna "order_value" de sales_df e, em seguida, chame o método .sum() para encontrar o valor total de todos os pedidos.
"""
import pandas as pd

# Read in sales.csv
sales_df = pd.read_csv("sales.csv")

# Print the mean order_value
print(sales_df["order_value"].mean())

# Print the total value of sales
print(sales_df["order_value"].sum())