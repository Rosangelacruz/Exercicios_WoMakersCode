# 3. Crie um dicionário representando um carrinho de compras. Adicione produtos(chaves) e quantidades (valores) ao carrinho. 
# Calcule o total do carrinho de compra.

# Criando um dicionário com produtos, suas quantidades e preços
carrinho_compras = {
    'Arroz': {'quantidade': 3, 'preco': 5.0},
    'Feijão': {'quantidade': 3, 'preco': 4.5},
    'Açúcar': {'quantidade': 2, 'preco': 2.0},
    'Macarrão': {'quantidade': 1, 'preco': 3.0},
    'Ovos': {'quantidade': 10, 'preco': 0.5}
}

# Calculando o valor total do carrinho de compras
valor_total = 0
for produto, info in carrinho_compras.items():
    quantidade = info['quantidade']
    preco = info['preco']
    valor_total += quantidade * preco

# Exibindo o valor total do carrinho de compras
print(f"Valor total do carrinho de compras: R$ {valor_total:.2f}")
    