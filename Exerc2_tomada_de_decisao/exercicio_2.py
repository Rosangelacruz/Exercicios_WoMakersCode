# 2. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutinoou V-Vespertino ou N-Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Solicita que o usuário informe em que tuno ele estuda
turno = input('Em que turno você estuda? (M-matutino, V-Vespertino, N-Noturno): ')

# Verifica o turno e imprime a mensagem correspondente
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido')