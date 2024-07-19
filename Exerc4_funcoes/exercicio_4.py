# 4. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia 
# comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02 
# Dólar Australiano: R$ 3,18 
# Dólar Canadense: R$ 3,64
# Franco Suiço: R$ 0,42 
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21

# Tabela de conversão
taxas_de_cambio = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

# Solicite ao usuário a digitar um valor em dinheiro 
valor_dinheiro = float(input("Digite o valor em dinheiro que você tem na carteira: "))

# Calcular e mostrar quantas moedas podem ser compradas
for moeda, taxa in taxas_de_cambio.items():
    quantidade = valor_dinheiro / taxa
    print(f"Você pode comprar {quantidade:.2f} de {moeda}.")
