# 3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius 
# para Fahrenheit ou vice - versa. Para cada opção,crie uma função. Plus: 
# Crie uma terceira,que é um menu para o usuário escolher a opção desejada,onde esse menu chama a função de conversão correta.

# Função para converter de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Função para converter de Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Função para exibir o menu de opções e realizar a conversão escolhida pelo usuário
def menu():
    while True:
        print('\nEscolha a operação que deseja realizar:')
        print('1 - Converter de Celsius para Fahrenheit')
        print('2 - Converter de Fahrenheit para Celsius')
        print('0 - Sair')
        escolha = input('Digite o número da opção desejada: ')

        if escolha == '1':
            celsius = float(input('Digite a temperatura em Celsius: '))
            resultado = celsius_para_fahrenheit(celsius)
            print(f'A temperatura de {celsius:.1f} °C é equivalente a {resultado:.1f} °F')

        elif escolha == '2':
            fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
            resultado = fahrenheit_para_celsius(fahrenheit)
            print(f'A temperatura de {fahrenheit:.1f} °F é equivalente a {resultado:.1f} °C')

        elif escolha == '0':
            print('Saindo do programa...')
            break

        else:
            print('Opção inválida. Por favor, digite novamente.')

# Chamando a função do menu para iniciar o programa
menu()