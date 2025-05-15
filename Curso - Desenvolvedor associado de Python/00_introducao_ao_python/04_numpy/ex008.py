"""Aritmética 2D
As matrizes 2D numpy podem realizar cálculos elemento a elemento, como as matrizes numpy.

np_baseball está codificado para você; trata-se novamente de uma matriz 2D do numpy com 3 colunas que representam altura (em polegadas), peso (em libras) e idade (em anos). baseball está disponível como uma lista de listas comum, e updated está disponível como uma matriz 2D do numpy.

Instruções

Você conseguiu obter as alterações de altura, peso e idade de todos os jogadores de beisebol. Estão disponíveis como uma matriz 2D do numpy, updated. Some np_baseball e updated e imprima o resultado.
Você deseja converter as unidades de altura e peso para o sistema métrico (metros e quilogramas, respectivamente). Como primeira etapa, crie uma matriz do numpy com três valores: 0.0254, 0.453592 e 1. Chame essa matriz de conversion.
Multiplique np_baseball por conversion e imprima o resultado."""

import numpy as np

baseball = [[74, 180], [74, 210], [72, 190], [72, 200], [70, 180], [70, 210], [69, 190], [68, 200], [68, 180], [67, 210],[67, 190], [66, 200], [66, 180], [65, 210], [65, 190], [64, 200], [64, 180], [63, 210], [63, 190], [62, 200], [62, 180], [61, 210], [61, 190], [60, 200], [60, 180], [59, 210], [59, 190], [58, 200],[58, 180], [57, 210], [57, 190], [56, 200], [56, 180], [55, 210], [55, 190], [54, 200], [54, 180], [53, 210], [53, 190], [52, 200], [52, 180], [51, 210], [51, 190], [50, 200], [50, 180], [49, 210], [49, 190], [48, 200], [48, 180], [47, 210], [47, 190], [46, 200], [46, 180], [45, 210], [45, 190], [44, 200], [44, 180], [43, 210], [43, 190], [42, 200],[42, 180], [41, 210], [41, 190], [40, 200], [40, 180], [39, 210], [39, 190], [38, 200], [38, 180], [37, 210], [37, 190], [36, 200], [36, 180], [35, 210], [35, 190], [34, 200], [34, 180], [33, 210], [33, 190], [32, 200], [32, 180], [31, 210], [31, 190], [30, 200], [30, 180], [29, 210], [29, 190], [28, 200], [28, 180], [27, 210], [27, 190], [26, 200], [26, 180], [25, 210], [25, 190], [24, 200], [24, 180], [23, 210], [23, 190], [22, 200], [22, 180], [21, 210], [21, 190], [20, 200], [20, 180], [19, 210], [19, 190], [18, 200], [18, 180], [17, 210], [17, 190], [16, 200], [16, 180], [15, 210], [15, 190], [14, 200], [14, 180], [13, 210], [13, 190], [12, 200], [12, 180], [11, 210], [11, 190], [10, 200], [10, 180], [9, 210], [9, 190], [8, 200],[8, 180]]

updated = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [0, 0, 6], [0, 0, 7], [0, 0, 8], [0, 0, 9],[0, 0, 10], [0, 0, 11], [0, 0, 12], [0, 0, 13], [0, 0, 14], [0, 0, 15], [0, 0, 16], [0, 0, 17], [0, 0, 18], [0, 1.5],[1.5 ,2.5 ,3.5],[4.5 ,5.5 ,6.5],[7.5 ,8.5 ,9.5],[10.5 ,11.5 ,12.5],[13.5 ,14.5 ,15.5],[16.5 ,17.5 ,18.5],[19.5 ,20.5 ,21.5],[22.5 ,23.5 ,24.5],[25.5 ,26.5 ,27.5]])

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)