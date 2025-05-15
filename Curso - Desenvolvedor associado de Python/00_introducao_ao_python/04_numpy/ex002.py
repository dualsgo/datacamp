"""Altura dos jogadores de beisebol
Você é um grande fã de beisebol. Você decide ligar para o site MLB (Major League Baseball) e pedir mais algumas estatísticas sobre a altura dos principais jogadores. Ela transmite dados sobre mais de mil jogadores, que são armazenados como uma lista comum do Python: height_in. A altura está expressa em polegadas. Você consegue criar uma matriz do numpy com ela e converter a unidade em metros?

height_in já está disponível e o pacote numpy está carregado, portanto você pode começar imediatamente (fonte: stat.ucla.edu).

Instruções

Crie uma matriz do numpy a partir de height_in. Chame essa nova matriz de np_height_in.
Imprima np_height_in.
Multiplique np_height_in por 0.0254 para converter todas as medidas de altura de polegadas em metros. Armazene os novos valores em uma nova matriz, np_height_m.
Imprima np_height_m e verifique se a saída faz sentido."""

# Import numpy
import numpy as np

height_in = [74, 74, 72, 72, 70, 70, 69, 68, 68, 67, 67, 66, 66, 65, 65]

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_heigth_m = np_height_in * 0.0254

# Print np_height_m
print(np_heigth_m)