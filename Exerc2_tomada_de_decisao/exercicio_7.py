# 7. Desenvolver um programa que solicite a idade do usuário e identifique se   ele é uma criança, um adolescente, adulto ou idoso.

# Silicitando ao usuário para digitar a sua idade 
idade = int(input('Digite a sua idade: '))

# verificando se é uma criança, um adolescente, adulto ou idoso.
if idade < 12:
    print('Você é uma criança.')
elif idade <18:
    print('Você é um adolescente.')
elif idade < 60:
    print('Você é um adulto.')
else:
    print('Você é um idoso.')