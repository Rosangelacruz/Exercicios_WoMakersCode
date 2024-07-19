# 9. O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. 
# O processo de leitura deve ser encerrado quando o usuário informar o valor zero. 
# Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.

 # Inicializar contadores
pares = 0
impares = 0

while True:
    # Solicitar ao usuário que digite um número
    num = float(input("Digite um número (ou zero para sair): "))

    # Verificar se o número é zero para encerrar o loop
    if num == 0:
        break

    # Verificar se o número é positivo
    if num > 0:
        # Verificar se o número é par ou ímpar
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        print("Número inválido. Por favor, insira apenas números positivos.")

# Apresentar os resultados
print(f"Quantidade de números pares: {pares}")
print('Programa encerrado com sucesso.')
