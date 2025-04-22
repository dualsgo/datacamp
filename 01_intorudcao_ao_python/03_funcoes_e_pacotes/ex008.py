"""Importação seletiva
As importações gerais, como import math, disponibilizam todas as funções do pacote math. No entanto, caso decida usar apenas uma parte específica de um pacote, sempre tem a opção tornar a importação mais seletiva:

from math import pi
Tente fazer a mesma coisa novamente, mas desta vez use apenas pi.

Instruções

Realize uma importação seletiva do pacote math importando apenas a função pi.
Use math.pi para calcular a circunferência do círculo e armazená-la em C.
Use math.pi para calcular a área do círculo e armazená-la em A."""

# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))