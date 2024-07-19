# 10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.

# Solicitar três números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Colocar os números em uma lista
numeros = [num1, num2, num3]

# Ordenar a lista em ordem crescente
numeros.sort()

# Exibir os números em ordem crescente
print("Os números em ordem crescente são:", (numeros[0], numeros[1], numeros[2]))