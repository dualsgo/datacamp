"""Atualização de uma variável com loops for
Você está planejando dar uma festa para mostrar sua playlist aos amigos e familiares. Você alugou um local com capacidade máxima de 30 pessoas e gostaria de controlar os ingressos vendidos.

Essa é a oportunidade perfeita para você usar um loop for: ele incrementará o valor de uma variável cada vez que um ingresso for vendido e, em seguida, imprimirá uma declaração quando o evento estiver esgotado.

Instruções
100 XP
Crie uma variável chamada tickets_sold com um valor de 0.
Crie uma variável chamada max_capacity com um valor de 30.
Percorra um intervalo começando em 1 e terminando em max_capacity mais um, nomeando o iterador como tickets.
Dentro do loop for, adicione 1 ao valor de tickets_sold."""

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for tickets in range(1, max_capacity+1):
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1
  
print("Sold out:", tickets_sold, "tickets sold!")