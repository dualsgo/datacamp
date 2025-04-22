"""Funcionamento interno das listas
Alguns códigos foram fornecidos para você neste exercício: uma lista com o nome areas e uma cópia chamada areas_copy.

Atualmente, o primeiro elemento da lista areas_copy é alterado e a lista areas é impressa. Se você pressionar o botão executar código, verá que, embora tenha alterado areas_copy, a alteração também terá efeito na lista areas. Isso ocorre porque areas e areas_copy apontam para a mesma lista.

Se quiser evitar que as alterações em areas_copy também tenham efeito em areas, você terá de fazer uma cópia mais explícita da lista areas com list() ou usando [:].

Instruções

Altere o segundo comando, que cria a variável areas_copy, de modo que areas_copy seja uma cópia explícita de areas. Após a edição, as alterações feitas em areas_copy não devem afetar areas. Envie a resposta para conferir.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)