# 3. Faça um Programa que peça aquantidade de quilômetros,
#transforme em metros 1000, centímetros 10,000 e milímetros 100,000.

# Solicita a quilometragem ao usuário e converte para float
quilometragem = float(input('Digite a quantidade de quilômetros: '))

# Realiza as operações de conversão
metros = quilometragem * 1000
centimetros = quilometragem * 100000
milimetros = quilometragem * 1000000

# Exibe os resultados
print(f'{quilometragem:.2f} quilômetros é igual a {metros:.2f} metros')
print(f'{quilometragem:.2f} quilômetros é igual a {centimetros:.2f} centímetros')
print(f'{quilometragem:.2f} quilômetros é igual a {milimetros:.2f} milímetros')