"""Substitua elementos de listas
Para substituir elementos da lista, você faz um subconjunto da lista e atribui novos valores ao subconjunto. Podemos selecionar elementos individuais ou alterar fatias inteiras da lista de uma só vez.

Neste e nos próximos exercícios, você continuará trabalhando na lista areas, que contém os nomes e as áreas dos diferentes cômodos de uma casa.

Instruções

Atualize a área do banheiro para que seja 10.50 metros quadrados em vez de 9.50 usando indexação negativa.
Torne a lista areas mais moderna! Altere "living room" para "chill zone". Não use indexação negativa desta vez."""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"