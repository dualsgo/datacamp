
"""Importando a partir de um módulo
Outro módulo útil datetime, que permite que você crie e trabalhe com datas e horas, bem como fusos horários e períodos de tempo!

O módulo datetime tem uma função chamada date.

Neste exercício, você praticará a importação e o uso do método date do módulo datetime e o usará para criar uma variável.

Instruções

Importe a função date do módulo datetime.
Crie uma variável chamada deadline, atribuindo uma chamada de date(), passando os números 2024, 1 e 19, nessa ordem, separados por vírgulas.

Verifique o tipo de dado de deadline.
Imprima a variável deadline."""

# Import date from the datetime module
from datetime import date

# Create a variable called deadline
deadline = date(2024, 1, 19)

# Check the data type
print(type(deadline))

# Print the deadline
print(deadline)