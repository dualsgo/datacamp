
"""Fazendo cálculos
As funções embutidas do Python facilitam a realização de cálculos com muitos valores sem que você precise escrever várias linhas de código.

Trabalhando com uma lista chamada course_completions que contém valores inteiros que representam o número de conclusões de uma série de cursos diferentes, você analisará esses dados para obter insights!

Some e imprima o número total de course_completions.

Imprima o maior valor em course_completions.

Some os valores em course_completions e, em seguida, divida-os pelo número de elementos para obter a média.

Arredonde o número médio de conclusões de curso para uma casa decimal.
"""



course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

# Print the total number of course completions
print(sum(course_completions))

# Print the largest number of completions
print(max(course_completions))

# Print the average number of completions
print(sum(course_completions) / len(course_completions))

# Print the average number of completions, rounded to one decimal places
print(round(sum(course_completions) / len(course_completions), 1))