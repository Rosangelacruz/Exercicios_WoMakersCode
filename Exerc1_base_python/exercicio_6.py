# 6. Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal(IMC)
# usando a fórmula: IMC = peso / (altura x altura).

# Solicitando ao usuário para digitar o peso em kg e a altura em metros
peso_kg = float(input('Digite o seu peso em kg: '))
altura_metros = float(input('Digite a sua altura em metros: '))

# Realizando a operação
imc = peso_kg / (altura_metros * altura_metros)

# Exibindo o resultado
print(f'O seu IMC é {imc:.2f}')
