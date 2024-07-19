# 1. Faça um programa, com uma função que necessite de três argumentos,e que forneça a soma desses três argumentos.
# Definindo a função que recebe três argumentos e retorna a soma

def soma_tres_numeros(a, b, c):
    return a + b + c

# Solicitando ao usuário que insira os três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Chamando a função com os números fornecidos pelo usuário
resultado = soma_tres_numeros(num1, num2, num3)

# Exibindo o resultado
print(f"A soma dos três números é: {resultado}")

# Exibindo o resultado
print(f"O reverso do número {numero} é: {resultado}")
