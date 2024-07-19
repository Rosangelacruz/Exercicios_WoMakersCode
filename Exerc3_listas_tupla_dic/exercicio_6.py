# 6. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente 
# utilizando somente letras maiúsculas. Dica: lembre−se que a o informar o nome ou suário pode digitar letras maiúsculas ou minúsculas.

# Solicitar ao usuário que digite o seu nome
nome = input("Digite o seu nome: ").strip()

# Converter o nome para letras maiúsculas e inverter a string
nome_invertido = nome.upper()[::-1]

# Exibir o nome invertido
print(f"Seu nome de trás para frente é: {nome_invertido}")
