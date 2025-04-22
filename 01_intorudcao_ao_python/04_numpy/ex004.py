"""Subdivisão de matrizes do NumPy
O subconjunto (usando a notação de colchetes em listas ou matrizes) funciona exatamente da mesma forma com listas e matrizes.

Este exercício já tem duas listas, height_in e weight_lb, carregadas em segundo plano para você. Elas contêm a altura e o peso dos jogadores do MLB como listas regulares. Ele também tem duas listas de matriz numpy, np_weight_lb e np_height_in, preparadas para você.

Instruções

Subdivida np_weight_lb imprimindo o elemento no índice 50.
Imprima uma submatriz de np_height_in que contenha os elementos no índice 100 até o índice 110 , incluindo este último."""

import numpy as np

weight_lb = [180, 215, 210, 188, 190, 200, 205, 195, 185, 175, 170, 160, 155, 150, 145, 140, 135, 130, 12, 120,
115, 110, 105, 100, 95, 90, 85, 80, 75, 70,
65, 60, 55, 50, 45, 40, 35, 30]

height_in = [74, 75, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45,  44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]


np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])