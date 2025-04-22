"""Sua primeira matriz do NumPy
Agora você vai mergulhar no mundo do beisebol. Ao longo do caminho, você se familiarizará com os conceitos básicos de numpy, um pacote avançado para fazer ciência de dados.

Uma lista baseball já foi definida no script Python, representando a altura de alguns jogadores de beisebol em centímetros. Você pode adicionar algum código para criar uma matriz numpy a partir dela?

Instruções

Importe o pacote numpy como np, para que você possa fazer referência a numpy com np.
Use np.array() para criar uma matriz numpy a partir de baseball. Chame essa matriz de np_baseball.
Imprima o tipo de np_baseball para conferir se está certo."""

# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))