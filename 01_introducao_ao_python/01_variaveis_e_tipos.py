# Atribuição de variáveis
# Em Python, uma variável permite que você faça referência a um valor com um nome. Para criar uma variável x com valor 5, usamos =, como neste exemplo:

x = 5

# Agora você pode usar o nome dessa variável, x, em vez do valor real, 5.
# Lembre-se de que = em Python significa atribuição, ele não testa a igualdade! 

# Crie uma variável savings com valor 100.
savings = 100

# Verifique essa variável digitando print(savings) no script.
print(savings)

# Cálculos com variáveis
# Agora que você criou uma variável chamada “savings”, vamos começar a economizar!
# Em vez de calcular com os valores reais, você pode usar variáveis.
#  Quanto dinheiro você teria economizado daqui a quatro meses, se tivesse economizado $10 todo mês?

# Crie uma variável monthly_savings igual a 10 e outra variável num_months igual a 4.
monthly_savings = 10
num_months = 4
# Multiplique monthly_savings por num_months e atribua-o a new_savings.
new_savings = monthly_savings * num_months

# Imprima o valor de new_savings.
print(new_savings)

# Outros tipos de variáveis
#No exercício anterior, você trabalhou com o tipo de dados número inteiro do Python:

# int ou inteiro: um número sem uma parte fracionária. savings, com valor 100, é um exemplo de número inteiro.
# Além dos tipos de dados numéricos, há três outros tipos de dados muito comuns:

# float ou ponto flutuante: número que tem uma parte inteira e uma parte fracionária, separadas por um ponto. 1.1 é um exemplo de float.
# str ou string: tipo usado para representar texto. Você pode usar aspas simples ou duplas para criar uma string.
# bool ou booleano: tipo usado para representar valores lógicos. Pode ser apenas True ou False (a distinção entre maiúsculas e minúsculas é importante!).

# Crie um novo float, half, com o valor 0.5.
half = 0.5

# Crie uma nova string, intro, com o valor "Hello! How are you?".
intro = "Hello! How are you?"

# Crie um novo booleano, is_good, com o valor True.
is_good = True

# Operações com outros tipos
# Em Python, as variáveis são de diferentes tipos. Você pode ver o tipo de uma variável usando type(). Por exemplo, para ver o tipo de a, execute: type(a).

# Tipos diferentes se comportam de forma diferente no Python. Ao somar duas strings, por exemplo, temos um comportamento diferente de quando somamos dois inteiros ou dois booleanos.

# É hora de você testar isso.
# Adicione savings e new_savings e atribua-o a total_savings.
total_savings = savings + new_savings

# Use type() para imprimir o tipo resultante de total_savings.
print(type(total_savings))

# Calcule a soma de intro e intro e atribua o resultado a doubleintro.
doubleintro = intro + intro

# Imprimir doubleintro. Você esperava por isso?
print(doubleintro)