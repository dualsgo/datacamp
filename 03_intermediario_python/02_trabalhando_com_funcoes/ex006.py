
"""Função do conversor de estrutura de dados
Agora que você aprendeu sobre os tipos de argumentos em funções, colocará isso em prática criando uma função personalizada que converte dados em diferentes estruturas.

Instruções

Defina convert_data_structure com dois argumentos: data e data_type, sendo que o último tem um valor padrão de "list".

Adicione uma condição para verificar se data_type é "tuple".

Caso contrário, se data_type for "set", converta data em um conjunto, salvando-o como uma variável de mesmo nome.

Chame a função na estrutura de dados fornecida, usando um par de valores de argumento de palavra-chave apropriado para convertê-la em um conjunto."""

# Create the convert_data_structure function
def convert_data_structure(data, data_type="list"):
  
  # If data_type is "tuple"
  if data_type == "tuple":
    data = tuple(data)
  
  # Else if data_type is set, convert to a set
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

# Call the function to convert to a set
convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")