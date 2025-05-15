"""Importação de pacote
Digamos que você queira calcular a circunferência e a área de um círculo. Veja a seguir como são essas fórmulas:

C = 2 * pi * r
A = pi * r**2

Em vez de digitar o número para pi, você pode usar o pacote math que contém o número

Para referência, ** é o símbolo de exponenciação. Por exemplo: 3**4 significa 3 elevado à 4.ª potência, que é igual a 81.

Instruções

Importe o pacote math.
Use math.pi para calcular a circunferência do círculo e armazená-la em C.
Use math.pi para calcular a área do círculo e armazená-la em A."""

# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))