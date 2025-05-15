"""Modificação de variáveis de string
Você se saiu tão bem trabalhando com as avaliações do LLM Camp que eles pediram sua ajuda novamente.

Eles têm uma variável chamada most_popular_course, que contém o nome do curso mais bem classificado. Ele foi fornecido em script.py para que você possa ver seu conteúdo. No entanto, há problemas com ele:

Há um erro de digitação. Deveria ser "Introduction" em vez de "Intro".
Eles querem remover os espaços e usar sublinhados para facilitar a análise.
Para fins de consistência, eles querem que todos os caracteres sejam minúsculos.
Eles gostariam de contar com o seu apoio para fazer essas mudanças!

Instruções 1/3

Atualize a variável de modo que "Intro" passe a ser "Introduction"."""

most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

print(most_popular_course)