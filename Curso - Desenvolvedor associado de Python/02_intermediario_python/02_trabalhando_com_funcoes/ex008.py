"""Docstrings multilinha
Às vezes, docstrings de uma única linha são suficientes, mas se a sua função for mais complexa ou tiver vários argumentos, geralmente é melhor usar uma docstring multilinha.

Você praticará isso criando uma docstring multilinha para a função convert_data_structure que você criou anteriormente.

Adicione um resumo à docstring: Convert a data structure to a list, tuple, or set..

Adicione Args:, primeiro com data (list, tuple, or set): A data structure to be converted., e depois com data_type (str): String representing the type of structure to convert data to.

Detalhe a seção Returns:: data (list, tuple, or set): Converted data structure.."""

# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure.
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))