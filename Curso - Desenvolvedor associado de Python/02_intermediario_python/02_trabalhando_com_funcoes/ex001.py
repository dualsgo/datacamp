
"""Sintaxe de função personalizada
Para criar uma função personalizada, você precisa seguir um processo repetível. Vamos verificar se você entende a sintaxe usada para concluir essa tarefa criando uma função para encontrar o maior valor em uma lista.

Instruções

Ordene e recue o código para criar uma função que classifique os dados e retorne o maior valor."""

def find_max_value(a_list):
    sorted_values = sorted(a_list)
    max_value = sorted_values[-1]
    return max_value