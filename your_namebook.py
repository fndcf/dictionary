#!/usr/bin/env python3

"""
Classe C que fornece método para transformar um dicionario em um array onde os nomes e sobrenome começam com letra maiuscula.

Métodos:
- array_of_names: Cria um array e transforma o nome e sobrenome em letra maiuscula 
- Printa o resultado do array criado no metodo array_of_names_
"""

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

class C:
    def array_of_names(self, array): # Cria um array e transforma o nome e sobrenome em letra maiuscula
        joined_result = ', '.join([f"{key.capitalize()} {value.capitalize()}" for key, value in array.items()]) #Cria uma string com os nomes e sobrenome separando por virgula
        transformed_array = joined_result.split(',') # Cria um array de nome e sobrenome
        return transformed_array

c = C()
c.array_of_names(persons) # Chama o metodo array_of_names com o parametro persons
print(f"{c.array_of_names(persons)}") # Printa um array de nome e sobrenome