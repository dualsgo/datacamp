"""Efeitos colaterais do NumPy
numpy é excelente para fazer aritmética vetorial. No entanto, se você comparar sua funcionalidade com as listas comuns do Python, algumas coisas mudaram.

Em primeiro lugar, as matrizes do numpy não podem conter elementos com tipos diferentes. Em segundo lugar, os operadores aritméticos típicos, como +, -, * e /, têm um significado diferente nas listas comuns do Python e matrizes do numpy.

Algumas linhas de código foram fornecidas para você. Experimente e escolha a que mais combina com você:

np.array([True, 1, 2]) + np.array([3, 4, False])
O pacote numpy já foi importado como np.

Instruções

Respostas possíveis

np.array([True, 1, 2, 3, 4, False])
np.array([4, 3, 0]) + np.array([0, 2, 2])
np.array([1, 1, 2]) + np.array([3, 4, -1])
np.array([0, 1, 2, 3, 4, 5])"""

import numpy as np
print(np.array([True, 1, 2]) + np.array([3, 4, False])
)