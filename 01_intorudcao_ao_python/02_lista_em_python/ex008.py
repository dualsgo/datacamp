"""Amplie uma lista
Você pode alterar os elementos de uma lista, mas também pode adicionar elementos a ela. Para fazer isso, utilize o operador +: Você pode usar o operador +:

x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
Você acabou de ganhar na loteria, incrível! Você decide construir um anexo à piscina e uma garagem. Você pode adicionar as informações à lista areas?

Instruções

Use o operador + para colar a lista ["poolhouse", 24.5] no final da lista areas. Armazene a lista resultante como areas_1.
Amplie ainda mais areas_1 adicionando dados sobre a garagem. Adicione a string "garage" e o float 15.45. Nomeie a lista resultante como areas_2."""

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]