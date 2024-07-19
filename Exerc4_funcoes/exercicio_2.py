# 2. Reverso do número.Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

# Definindo a função que retorna o reverso de um número inteiro
def reverso_numero(numero):

# Convertendo o número para string, invertendo a string e convertendo de volta para inteiro
    numero_reverso = int(str(numero)[::-1])
    return numero_reverso

# Solicitando ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Chamando a função e armazenando o resultado
resultado = reverso_numero(numero)

# Exibindo o resultado
print(f"O reverso do número {numero} é: {resultado}")
