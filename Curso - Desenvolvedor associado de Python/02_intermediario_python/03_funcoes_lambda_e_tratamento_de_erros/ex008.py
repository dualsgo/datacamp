"""Retorno de erros
É hora de experimentar a outra abordagem para o tratamento de erros.

Edite a função snake_case() para produzir intencionalmente um erro se um tipo de dados incorreto for usado.

Instruções

Verifique se o tipo de dados do argumento text é string str.

Dentro do bloco else, produza um TypeError() para impedir a execução do script e retornar uma mensagem descritiva.
"""

def snake_case(text):
  # Check the data type
  if isinstance(text, str):
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")