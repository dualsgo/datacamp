"""Lista de listas
Como cientistas de dados, geralmente lidamos com muitos dados, e faz sentido agrupar alguns deles.

Em vez de criar uma lista contendo strings e floats, representando os nomes e as áreas dos cômodos da sua casa, você pode criar uma lista de listas.

Lembre-se: "hallway" é uma cadeia de caracteres, enquanto hall é uma variável que representa o float 11.25 que você especificou anteriormente.

Instruções

Termine a lista de listas para que ela também contenha os dados do quarto (bedroom) e do banheiro (bathroom). Lembre-se de inseri-los em ordem!
Imprima house; essa forma de estruturar os dados faz mais sentido?
"""

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]
         ]

# Print out house
print(house)