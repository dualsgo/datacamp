"""Métodos de listas
As strings não são os únicos tipos Python que têm métodos associados a elas. Listas, floats, inteiros e booleanos também são tipos que vêm com vários métodos úteis. Neste exercício, você fará experiências com:

.index()para obter o índice do primeiro elemento de uma lista que corresponde à sua entrada e
.count()para obter o número de vezes que um elemento aparece em uma lista.
Você trabalhará na lista com a área de diferentes partes de uma casa: areas.

Instruções

Use o método .index() para obter o índice do elemento em areas que é igual a 20.0. Imprima esse índice.
Ligue para .count() em areas para saber quantas vezes 9.50 aparece na lista. Novamente, basta imprimir esse número."""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))