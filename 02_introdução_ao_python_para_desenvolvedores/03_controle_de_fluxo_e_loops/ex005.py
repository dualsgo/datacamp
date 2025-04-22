"""Loop condicional com um dicionário
Seu amigo do LLM Camp forneceu a você um dicionário chamado courses. Ele contém os nomes dos cursos como chaves e o tópico associado a eles como um valor. Há três tópicos: "AI", "Programming", e "Data Engineering".


courses = {"LLM Concepts": "AI", 

           "Introduction to Data Pipelines": "Data Engineering", 

           "AI Ethics": "AI",

           "Introduction to dbt": "Data Engineering", 

           "Writing Efficient Python Code": "Programming",

           "Introduction to Docker": "Programming"}
Essa é uma ótima oportunidade para você praticar o loop nos dicionários!

Instruções

Crie um loop for para iterar sobre key, value em courses.items().
Verifique se value é "AI" e, se for o caso, imprima key.
Caso contrário, verifique se value é "Programming", imprimindo a key se for o caso.
Caso contrário, imprima a key para confirmar que se trata de um curso de "Data Engineering"."""

courses = {"LLM Concepts": "AI", 
           "Introduction to Data Pipelines": "Data Engineering", 
           "AI Ethics": "AI",
           "Introduction to dbt": "Data Engineering", 
           "Writing Efficient Python Code": "Programming",
           "Introduction to Docker": "Programming"}

# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value == "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value == "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")