"""Argumentos arbitrários de palavras-chave
Argumentos posicionais arbitrários são uma maneira de adicionar flexibilidade ao criar funções personalizadas, mas você também pode usar argumentos arbitrários de palavras-chave.

Seu objetivo é usar a função concat que você criou no último exercício e modificá-la para aceitar argumentos arbitrários de palavras-chave. Boa sorte!

Instruções

Defina concat() como uma função que aceita argumentos de palavras-chave arbitrárias chamadas kwargs.

Dentro da função, crie uma string vazia.
Dentro da função, faça um loop sobre os valores do argumento da palavra-chave, usando kwarg como iterador.

Chame concat() com argumentos de palavra-chave de start igual a "Python", middle igual a "is" e end igual a "great!"."""


# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for arg in kwargs:
    result += " " + kwargs[arg]
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))