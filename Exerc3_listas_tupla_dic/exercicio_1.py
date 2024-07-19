# 1. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 

"""Telefonou para a vítima?""" 
"""Esteve no local do crime?"""
"""Mora perto da vítima?"""
"""Devia para a vítima?"""
"""Já trabalhou com a vítima?"""

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", 
# entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"". Caso contrário, ele será classificado como ""Inocente"".

# Lista de perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Inicializa contador de respostas positivas
respostas_positivas = 0

# Loop para fazer as perguntas e registrar as respostas
for pergunta in perguntas:
    resposta = input(f"{pergunta} (sim/não): ").strip().lower()
    if resposta == "sim":
        respostas_positivas += 1

# Classificação da participação
if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")