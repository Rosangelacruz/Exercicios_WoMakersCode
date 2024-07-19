# 4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida.
# Calcule e imprima o consumo médio em km/l.

# Solicitando ao usuário para digitar a  quantidade de litros de combustível consumidos e a distância percorrida
litros_combustivel = float(input('Digite a quantidade de litros de combustível consumidos: '))
distancia = float(input('Digite a distâcia pecorrida: '))

## Realize a operações
consumo_medio = distancia / litros_combustivel

# Exibe o resultado
print(f'O consumo meédio é de {consumo_medio:.2}')
