
"""Trabalhando com pandas
pandas é um exemplo de um pacote Python popular.

Neste exercício, o dicionário sales foi criado e disponibilizado para você, e sua tarefa é convertê-lo em um DataFrame do pandas e visualizar as cinco primeiras linhas.

Instruções

Importe o módulo pandas usando um alias de pd.
Crie sales_df usando uma função pandas para converter sales em um DataFrame.
Visualize as cinco primeiras linhas de sales_df."""

# Import pandas as pd
import pandas as pd

sales = {
    'product': ['A', 'B', 'C', 'D', 'E'],
    'sales': [100, 200, 300, 400, 500],
    'profit': [10, 20, 30, 40, 50],
    'region': ['North', 'South', 'East', 'West', 'Central']
}

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_df.head())