# 3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.

# Solicita que o usuário informe uma nota entre 0 e 10 até que o valor seja válido
while True:
    try:
        nota = float(input('Digite uma nota entre 0 e 10: '))

        if 0 <= nota <= 10:
            print(f"A nota inserida é: {nota}")
            break
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Por favor, insira um número válido.")
