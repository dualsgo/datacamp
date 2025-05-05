"""
Contagem dos elementos
No vídeo, você viu algumas das funções embutidas mais úteis do Python.

Uma delas pode ser usada para contar o número de elementos em uma variável. Você vai ver três variáveis nas etapas a seguir:

course_ratings - uma variável de dicionário que contém os nomes dos cursos como chaves e as notas médias como valores.

course_completions - uma variável de lista que contém o número diário de conclusões de um curso individual.

most_popular_course - uma variável do tipo string que contém o nome de um curso.
Você vai aplicar essa função às três variáveis!

Instruções 3/3

Use uma função para contar o número de pares de valor-chave em course_ratings, armazenando-os como uma variável chamada num_courses e, em seguida, imprima a variável.

Use uma função para contar o número de cursos em course_completions, armazenando como num_courses, e imprima essa variável.

Use uma função para contar o número de caracteres em most_popular_course, armazenando como title_length, e imprima a variável.
"""

course_ratings = {"LLM Concepts": 4.7, 
                  "Introduction to Data Pipelines": 4.75, 
                  "AI Ethics": 4.62, 
                  "Introduction to dbt": 4.81}

# Print the number of key-value pairs
num_courses = len(course_ratings)
print(num_courses)

course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

# Find the number of courses
num_courses = len(course_completions)
print(num_courses)

most_popular_course = "Introduction to dbt"

# How many characters are in most_popular_course?
title_length = len(most_popular_course)
print(title_length)