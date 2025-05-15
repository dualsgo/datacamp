"""Subdivida para conquistar
É muito fácil subdividir listas Python. Veja o exemplo de código abaixo, que cria uma lista x e, em seguida, seleciona "b" nela. Lembre-se de que esse é o segundo elemento, portanto tem índice 1. Você também pode usar a indexação negativa.

x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
Lembra-se da lista areas de antes, que contém strings e floats? Sua definição já está no script. Você pode adicionar o código correto para fazer uma subdivisão em Python?

Instruções

Imprima o segundo elemento da lista areas (ele tem o valor 11.25).
Crie um subconjunto e imprima o último elemento de areas, que é 9.50. Aqui faz sentido usar um índice negativo!
Selecione o número que representa a área da sala de estar (20.0) e imprima-o"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])