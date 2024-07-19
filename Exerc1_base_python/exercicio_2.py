# 2. Peça ao usuário para informar o ano de nascimento.
# Em seguida, calcule e imprima a idade atual.

# Solicita o ano de nascimento ao usuário converter para int
ano_nacimento = int(input('Digite o seu ano de nascimento: '))

# Realiza as operações
ano_atual = 2024
subtracao = ano_atual - ano_nacimento
print(f'A idade atual {subtracao} anos')