#!/usr/bin/env python3

"""
Classe C que fornece método para mostrar o "name" e o "date_of_birth" do dicionario.
Método:
- famous_births: recebe um dicionário e imprime os cientistas ordenados pela data de nascimento.
"""

# Dicionário contendo informações sobre cientistas mulheres, onde a chave é um identificador e o valor é outro dicionário
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },  
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },  
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },  
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }   
}

# Definindo a classe C
class C:
    # Método que imprime os cientistas ordenados pela data de nascimento
    def famous_births(self, historical_figures):
        # Ordena os figuras históricas pela data de nascimento (key=lambda x: x['date_of_birth'])
        sorted_figure = sorted(historical_figures.values(), key=lambda x: x['date_of_birth'])
        # Itera sobre cada figura ordenada e imprime seu nome e data de nascimento
        for scientist in sorted_figure:
            print(f"{scientist['name']} is a great scientist born in {scientist['date_of_birth']}")

# Instanciando a classe C
c = C()
# Chamando o método famous_births com o dicionário women_scientists
c.famous_births(women_scientists)
