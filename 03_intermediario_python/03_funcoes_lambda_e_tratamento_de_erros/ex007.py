
"""Exercício
Evite erros
No vídeo, você viu algumas abordagens de tratamento de erros que podem ser aplicadas a funções personalizadas.

Neste exercício, você testará uma das abordagens que evita gerar um erro, imprimindo uma mensagem útil se ocorrer um erro, mas não encerrando o script.

Instruções

Use uma palavra-chave que permita que você tente executar o código que limpa text.

Troque um espaço por um único sublinhado no argumento text.

Use outra palavra-chave que imprima uma mensagem útil se ocorrer um erro ao chamar a função snake_case()"""

def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace("", "_")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")