"""Convertesão em um loop while
Muitas vezes, você pode realizar as mesmas tarefas usando um loop for ou while.

Para demonstrar isso, você converterá esse loop for em um while!

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 10

# Loop through a range up to and including max_capacity's value
for tickets in range(1, max_capacity + 1):

  # Add one to tickets_sold in each iteration

  tickets_sold += 1


print("Sold out:", tickets_sold, "tickets sold!")
Observe que, se o loop while demorar muito para ser executado ou se a sessão estiver expirando, você poderá ter criado um loop infinito. Em particular, lembre-se de recuar o conteúdo do loop usando quatro espaços ou recuo automático, e certifique-se de que as condições sejam tais que o loop tenha um ponto de parada.

Instruções

Crie um loop while para ser executado enquanto tickets_sold for menor que max_capacity.
Dentro do loop, incremente tickets_sold em 1, representando um aumento para cada ingresso vendido.
Fora do loop, imprima tickets_sold"""

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 10

# Loop through a range up to and including max_capacity's value
for tickets in range(1, max_capacity + 1):
    
  # Add one to tickets_sold in each iteration
  tickets_sold += 1
  
# ------------------------------------------------------------------ #

tickets_sold = 0
max_capacity = 10

# Create a while loop
while tickets_sold < max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!") 