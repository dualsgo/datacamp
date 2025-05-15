"""Exclua elementos de uma lista
Por fim, também podemos remover elementos de uma lista. Podemos fazer isso com a instrução del:

x = ["a", "b", "c", "d"]
del x[1]
Preste atenção: assim que removemos um elemento de uma lista, todos os índices dos elementos que vêm depois do item excluído são alterados!

Infelizmente, o valor que você ganhou na loteria não é tão grande assim e parece que a casa da piscina não vai acontecer. Você precisará removê-lo da lista. Você decide remover a string e o float correspondentes da lista areas.

Instruções

Exclua a string e o float para "poolhouse" da lista areas.
Imprima a lista atualizada do site areas.
"""

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10:12]

# Print the updated list
print(areas)