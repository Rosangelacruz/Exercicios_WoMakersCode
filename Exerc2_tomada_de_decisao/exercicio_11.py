# 11. Escreva um programa que calcule o salário líquido.Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.

# ● Renda até R$1.903,98: isento de imposto de renda;
# ● Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%; 
# ● Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%; 
# ● Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%;
# ● Renda acima de R$4.664,68: alíquota máxima de 27,5%

# Solicitar ao usuário que informe o salário bruto
salario_bruto = float(input("Digite o salário bruto: "))

# Calcular o Imposto de Renda de acordo com as faixas
if salario_bruto <= 1903.98:
    imposto_renda = 0
elif salario_bruto <= 2826.65:
    imposto_renda = salario_bruto * 0.075 - 142.8
elif salario_bruto <= 3751.05:
    imposto_renda = salario_bruto * 0.15 - 354.8
elif salario_bruto <= 4664.68:
    imposto_renda = salario_bruto * 0.225 - 636.13
else:
    imposto_renda = salario_bruto * 0.275 - 869.36

# Calcular o salário líquido
salario_liquido = salario_bruto - imposto_renda

# Exibir o salário líquido e o valor do Imposto de Renda
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")