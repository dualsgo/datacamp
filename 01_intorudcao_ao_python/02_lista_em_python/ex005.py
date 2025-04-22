"""Fatiamento e divisão
A seleção de valores individuais em uma lista é apenas uma parte da história. Também é possível fatiar a lista, o que significa selecionar vários elementos da lista. Use a seguinte sintaxe:

my_list[start:end]
O índice start será incluído, enquanto o índice end não será. No entanto, também há a opção de não especificar esses índices. Se você não especificar o índice start, o Python entenderá que você deseja iniciar a fatia no início da lista.

Instruções

Use o fatiamento para criar uma lista, downstairs, que contém os primeiros 6 elementos de areas.
Crie upstairs, com os últimos elementos de 4 de areas. Desta vez, simplifique o fatiamento omitindo o índice end.
Imprima os sites downstairs e upstairs usando print()."""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)