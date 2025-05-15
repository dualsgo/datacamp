
"""Docstrings de uma linha
Docstrings são usadas para explicar a finalidade de uma função. Embora o nome da função deva ser descritivo, isso precisa ser equilibrado com o tamanho do nome da função, por isso as docstrings permitem que você forneça mais detalhes.

Neste exercício, você usará a função clean_text criada anteriormente e adicionará uma docstring de linha única.

Instruções
Adicione uma docstring informando "Swap spaces to underscores and convert text to lowercase.".

Acesse a docstring da função usando o atributo apropriado."""

def clean_string(text):
  
  # Add a single-line docstring
  """Swap spaces to underscores and convert text to lowercase"""
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)