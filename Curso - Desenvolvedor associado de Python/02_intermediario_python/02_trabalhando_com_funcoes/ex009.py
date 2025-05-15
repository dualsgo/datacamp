"""Adicionando argumentos arbitrários
No vídeo, você viu que o Python permite que as funções personalizadas aceitem qualquer número de argumentos posicionais por meio do uso de "argumentos arbitrários". Essa flexibilidade permite que as funções sejam usadas de várias maneiras e ainda produzam os resultados esperados!

Usando esse poder, você criará uma função que concatena (une) strings, independentemente de quantos blocos de texto forem fornecidos!

Instruções

Defina uma função chamada concat() que aceite argumentos arbitrários chamados args.

Crie uma variável chamada result e atribua a ela uma string vazia.

Use um loop for para iterar sobre cada arg em args.
Chame a função para testar se ela está funcionando corretamente."""

# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))