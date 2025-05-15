"""Diferentes formas de importação
Há várias maneiras de importar pacotes e módulos no Python. Dependendo da chamada de importação, deve ser usado um código Python diferente.

Suponha que você queira usar a função inv(), que está no subpacote linalg do pacote scipy. Você deseja poder usar essa função da seguinte forma:

my_inv([[1,2], [3,4]])
Qual instrução import é necessária para executar o código acima sem erros?

Instruções
Respostas possíveis

import scipy
import scipy.linalg
from scipy.linalg import my_inv
from scipy.linalg import inv as my_inv"""

from scipy.linalg import inv as my_inv