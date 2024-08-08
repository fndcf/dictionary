#!/usr/bin/env python3

"""
Classe C que fornece método para pegar as notas vindas de um dicionario e calcular a media da sala
Método:
- average: recebe um dicionario, faz a soma as notas dos values que estão no dicionario e faz a media
"""

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

class C:
    def average(self, dictionary): # Cria a media da sala com base nas notas dos alunos
        sum_grades = sum(dictionary.values()) # Faz a soma dos valores do dicionario
        avg = sum_grades / len(dictionary.values()) # Faz a media da sala com base no len 
        return avg # Retorna a media
    
c = C()
print(f"Average for class 3B: {c.average(class_3B)}.") # Printa a media da classe 3B
print(f"Average for class 3C: {c.average(class_3C)}.") # Printa a media da classe 3C