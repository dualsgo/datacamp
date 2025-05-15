
"""Adição de imposto
É hora de testar suas habilidades com a função lambda!

Neste exercício, você usará uma função lambda para adicionar um imposto de 20% ao custo da variável sale_price.

Instruções

Defina a função lambda add_tax para multiplicar o argumento fornecido a ela, x, por 1.2.

Chame add_tax() na variável sale_price."""

sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x*1.2

# Call the lambda function
print(add_tax(sale_price))