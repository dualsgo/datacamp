"""Sua primeira matriz 2D do NumPy
Antes de trabalhar nos dados reais do MLB, vamos tentar criar uma matriz 2D numpy a partir de uma pequena lista de listas.

Neste exercício, baseball é uma lista de listas. A lista principal contém 4 elementos. Cada um desses elementos é uma lista que contém a altura e o peso de 4 jogadores de beisebol, nessa ordem. baseball já está codificado para você no script.

Instruções

Use np.array() para criar uma matriz 2D numpy a partir de baseball. Chame-o de np_baseball.
Imprima o tipo de np_baseball.
Imprima o atributo shape de np_baseball. Use np_baseball.shape"""

import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)