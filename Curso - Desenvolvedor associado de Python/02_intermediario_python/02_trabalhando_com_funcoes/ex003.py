
"""Criação de um verificador de senhas
Você viu como as instruções condicionais podem ser usadas para verificar a igualdade. Agora que você tem as habilidades para criar uma função personalizada, combinará essas duas técnicas para criar uma função chamada password_checker que compara a senha de um usuário a um valor enviado, imprimindo condicionalmente uma saída dependendo do resultado.

Instruções
Defina a função password_checker, que deve aceitar um argumento chamado submission.

Verifique se password é igual a submission.

Adicione uma palavra-chave que permita a impressão condicional de "Incorrect password" se password e submission forem diferentes.

Chame a função, passando "NOT_VERY_SECURE_2023"."""

password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if password == submission:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker("NOT_VERY_SECURE_2023")