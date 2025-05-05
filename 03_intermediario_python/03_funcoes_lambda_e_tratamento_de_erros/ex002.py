
"""Chamando lambda em linha
Lembre-se de que um dos principais benefícios da lambda é a capacidade de usar funções em linha.

Neste exercício, você modificará a abordagem do exercício anterior para adicionar imposto à variável sales_price em linha sem armazenar uma função lambda como variável primeiro.

Instruções

Em uma única linha de código, crie uma função lambda que multiplique sale_price por 1,2 e retorne o resultado."""

sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x, y: x * y)(sale_price, 1.2))