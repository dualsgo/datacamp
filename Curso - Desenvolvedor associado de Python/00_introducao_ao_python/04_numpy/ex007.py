"""Subdivisão de matrizes 2D do NumPy
Se sua matriz 2D do numpy tiver uma estrutura regular, ou seja, cada linha e coluna tiver um número fixo de valores, as formas complicadas de subdivisão ficarão muito fáceis. Dê uma olhada no código abaixo, em que os elementos "a" e "c" são extraídos de uma lista de listas.

# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
Os índices antes da vírgula se referem às linhas, enquanto os índices após a vírgula se referem às colunas. O : serve para fatiar; neste exemplo, ele diz ao Python para incluir todas as linhas.

Instruções

Imprima a 50ª linha de np_baseball.
Crie uma nova variável, np_weight_lb, contendo a segunda coluna inteira de np_baseball.
Selecione a altura (primeira coluna) do 124º jogador de beisebol em np_baseball e imprima-a."""

import numpy as np

baseball = [[74, 180], [74, 210], [72, 190], [72, 200], [70, 180], [70, 210], [69, 190], [68, 200], [68, 180], [67, 210],[67, 190], [66, 200], [66, 180], [65, 210], [65, 190], [64, 200], [64, 180], [63, 210], [63, 190], [62, 200], [62, 180], [61, 210], [61, 190], [60, 200], [60, 180], [59, 210], [59, 190], [58, 200],[58, 180], [57, 210], [57, 190], [56, 200], [56, 180], [55, 210], [55, 190], [54, 200], [54, 180], [53, 210], [53, 190], [52, 200], [52, 180], [51, 210], [51, 190], [50, 200], [50, 180], [49, 210], [49, 190], [48, 200], [48, 180], [47, 210], [47, 190], [46, 200], [46, 180], [45, 210], [45, 190], [44, 200], [44, 180], [43, 210], [43, 190], [42, 200],[42, 180], [41, 210], [41, 190], [40, 200], [40, 180], [39, 210], [39, 190], [38, 200], [38, 180], [37, 210], [37, 190], [36, 200], [36, 180], [35, 210], [35, 190], [34, 200], [34, 180], [33, 210], [33, 190], [32, 200], [32, 180], [31, 210], [31, 190], [30, 200], [30, 180], [29, 210], [29, 190], [28, 200], [28, 180], [27, 210], [27, 190], [26, 200], [26, 180], [25, 210], [25, 190], [24, 200], [24, 180], [23, 210], [23, 190], [22, 200], [22, 180], [21, 210], [21, 190], [20, 200], [20, 180], [19, 210], [19, 190], [18, 200], [18, 180], [17, 210], [17, 190], [16, 200], [16, 180], [15, 210], [15, 190], [14, 200], [14, 180], [13, 210], [13, 190], [12, 200], [12, 180], [11, 210], [11, 190], [10, 200], [10, 180], [9, 210], [9, 190], [8, 200],[8, 180]]

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Print out height of 124th player
print(np_baseball[123, 0])