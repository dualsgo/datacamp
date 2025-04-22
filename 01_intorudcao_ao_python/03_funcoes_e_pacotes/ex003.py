"""Vários argumentos
No exercício anterior, você identificou argumentos opcionais ao visualizar a documentação com help(). Agora você aplicará isso para alterar o comportamento da função sorted().

Dê uma olhada na documentação de sorted() digitando help(sorted) no IPython Shell.

Você verá que sorted() recebe três argumentos: iterable, key, e reverse. Neste exercício, você só precisa especificar iterable e reverse, e não key.

Duas listas foram criadas para você.

Você pode combiná-las e classificá-las em ordem decrescente?

Instruções

Use + para combinar o conteúdo de first e second em uma nova lista: full.
Chame sorted() e em full e especifique o argumento reverse para ser True. Salve a lista ordenada como full_sorted.
Para finalizar, imprima full_sorted."""

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)