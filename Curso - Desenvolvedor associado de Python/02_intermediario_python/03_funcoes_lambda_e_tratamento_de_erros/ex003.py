
"""Funções lambda com iteráveis
Você usou as funções lambda para executar ações em um único valor; agora é hora de testar como trabalhar com iteráveis.

Você recebeu uma lista chamada sales_prices que contém os preços de venda de vários itens. Seu objetivo é usar uma função lambda para adicionar o imposto (20%) a cada valor da lista.

Instruções

Crie add_taxes, que multiplica cada valor em sales_prices por 20%.

Imprima uma lista usando add_taxes para atualizar os valores em sales_prices.
"""

sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Use add_taxes to return a new list with updated values
print(list(add_taxes))