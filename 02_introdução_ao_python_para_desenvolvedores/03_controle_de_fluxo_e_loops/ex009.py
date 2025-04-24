"""Trabalhando com palavras-chave
Trabalhando novamente com o dicionário genre_sales, desta vez você aplicará várias condições simultaneamente para descobrir informações sobre gêneros de livros e vendas médias!

Instruções 1/2

Percorra as chaves e os valores do dicionário genre_sales.
Dentro do loop, verifique se o gênero é "Horror" ou "Mystery".
Verifique se o gênero é "Thriller" e se a média de vendas é maior ou igual a 3000000.
"""

genre_sales = {
    "Fiction": 5166000000,
    "Non-Fiction": 80000000,
    "Science Fiction": 2000000000,
    "Fantasy": 1500000000,
    "Mystery": 1200000000,
    "Romance": 900000000,
    "Thriller": 1100000000,
    "Horror": 500000000,
}

# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  
  # Check if genre is Thriller and sale is at least 3 million
  elif genre == "Thriller" and sale >= 3000000:
    print(genre, sale)