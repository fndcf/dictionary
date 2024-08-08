#!/usr/bin/env python3

"""
Classe C que fornece método para transformar um dicionario em um array onde mostra os nomes de quem tem cabelo vermelho

Métodos:
- find_the_redheads: Cria um array e transforma o nome e sobrenome em letra maiuscula 
- Printa o resultado do array criado no metodo array_of_names_
"""

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

class C:
    def find_the_redheads(self, array): # Cria um array com pessoas que tem o cabelo vermelho
        red_names = dict(filter(lambda x:x[1]=='red', array.items())) #Cria um dicionario que filtra o nome das pessoas que tem cabelo vermelho
        names = list(red_names.keys()) #Cria uma variavel que retorna as pessoas que tem o cabelo vermelho em uma lista
        return names
    
c = C()
c.find_the_redheads(dupont_family) # Chama o metodo afind_the_redheads com o parametro dupont_family
print(f"{c.find_the_redheads(dupont_family)}") # Printa um array com o nome das pessoas que tem o cabelo vermelho