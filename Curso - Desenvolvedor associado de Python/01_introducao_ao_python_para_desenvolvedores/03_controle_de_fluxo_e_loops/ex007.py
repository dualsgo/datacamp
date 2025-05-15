"""
Anexar a uma lista
Você recebeu um dicionário chamado authors, que contém informações sobre 20 dos autores de ficção mais populares do mundo. Ele contém os nomes dos autores como chaves e o número de livros que eles criaram como valores.

Você está interessado em descobrir quantos desses autores produziram menos de 25 livros. Para fazer isso, você criará uma lista chamada authors_below_twenty_five, preenchendo-a com nomes de autores condicionalmente com base no fato de eles terem criado menos de 25 livros.

Instruções
Crie uma lista vazia chamada authors_below_twenty_five.
Percorra os iteradores key e value no dicionário authors.
Dentro do loop for, verifique se o iterador value é menor que 25.
Se for o caso, acrescente o nome do autor à lista authors_below_twenty_five."""

authors = {
    "Agatha Christie": 85,
    "Stephen King": 63,
    "J.K. Rowling": 7,
    "George R.R. Martin": 5,
    "Isaac Asimov": 500,
    "Arthur C. Clarke": 100,
    "Ray Bradbury": 27,
    "J.R.R. Tolkien": 4,
    "C.S. Lewis": 30,
    "Margaret Atwood": 16,
    "Neil Gaiman": 20}

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
  # Check for values less than 25
  if value < 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)