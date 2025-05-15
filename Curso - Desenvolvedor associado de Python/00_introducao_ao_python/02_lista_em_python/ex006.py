"""Subdivisão de listas de listas
Uma lista Python também pode conter outras listas.

Para subdividir listas de listas, podemos usar a mesma técnica de antes: colchetes. Para uma lista, isso seria parecido com o seguinte: house:

house[2][0]
Instruções

Faça um subconjunto da lista house para obter o float 9.5."""

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[4][1]