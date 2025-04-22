"""Métodos de strings
As strings vêm com vários métodos. Siga atentamente as instruções para descobrir alguns. Se quiser descobri-los com mais detalhes, você sempre tem a opção de digitar help(str) no Shell IPython.

Uma string place já foi criada para você experimentar.

Instruções

Use o método .upper() em place e armazene o resultado em place_up. Use a sintaxe para chamar métodos que você aprendeu no vídeo anterior.
Imprima place e place_up. Ambas mudaram?
Imprima o número de o's na variável place chamando .count() em place e passando a letra 'o' como entrada para o método. Estamos falando da variável place, não da palavra "place"!"""

# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)


# Print out the number of o's in place
print(place.count('o'))