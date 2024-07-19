# 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

# Criando lista
meses_validos = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Solicitando ao usuário o mês atual
mês = input('Digite o mês atual: ').strip().lower()

if mês in meses_validos:
    print(f"O mês atual é {mês.capitalize()}.")
else:
    print("Mês inválido. Por favor, digite o nome de um mês válido.")

# Solicitando ao usuário quanto você ganha por hora e o número de horas trabalhadas no mês
salario_hora = float(input('Digite o valor de seu salario por hora: '))
hora_trabalhada = float(input('Digite o seu numero de horas trabalhadas no mês: '))

# Realize a oeração
salario_mes = salario_hora * hora_trabalhada

# Exibindo o resultado
print(f'O seu salário no mês é {salario_mes:.2f}')
