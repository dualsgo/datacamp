"""Métodos de listas (2)
A maioria dos métodos de listas altera a lista em que são chamados. Alguns exemplos são:

.append()que adiciona um elemento à lista em que é chamado,
.remove()que remove o primeiro elemento de uma lista que corresponde à entrada, e
.reverse()que inverte a ordem dos elementos da lista em que é chamado.
Você trabalhará na lista com a área de diferentes partes da casa: areas.

Instruções

Use .append() duas vezes para adicionar o tamanho da casa da piscina e da garagem novamente: 24.5 e 15.45, respectivamente. Lembre-se de adicioná-los nesta ordem.
Imprima areas.
Use o método .reverse() para inverter a ordem dos elementos em areas.
Imprima areas mais uma vez.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)