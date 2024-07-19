# 8. Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total
# de calorias queimadas em um mês, considerando uma média de 5 calorias por minutos de exercício.

# Solicitando ao usuário o número de horas de exercício físico por semana
hora_exercicio = float(input('Digite a quantida de horas de exercicio por semana: '))

# Realize a operação
total_calorias = hora_exercicio * 5

# Exibindo o resultado
print(f'O total de calorias queimadas em um mês é {total_calorias:.2f}')